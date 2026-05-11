#!/usr/bin/env python3
"""
Telegram smoke test for Prufrock experiment 0.

Validates the bot token, discovers your chat ID from recent messages,
clears any stale webhook, sends a Hello World message, and prints the
exact values you need for your .env file.

Usage:
    python3 deploy/smoke-test-telegram.py --token 123456:ABC...
    python3 deploy/smoke-test-telegram.py          # reads TELEGRAM_BOT_TOKEN from env or .env
"""

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


# ── Telegram API helper ───────────────────────────────────────────────────────

def _api(token: str, method: str, payload: dict | None = None, timeout: int = 10) -> dict:
    url = f"https://api.telegram.org/bot{token}/{method}"
    data = json.dumps(payload).encode() if payload else None
    headers = {"Content-Type": "application/json"} if data else {}
    req = urllib.request.Request(url, data=data, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as exc:
        return json.loads(exc.read())
    except urllib.error.URLError as exc:
        reason = str(exc.reason)
        if "CERTIFICATE_VERIFY_FAILED" in reason or "SSL" in reason.upper():
            print(f"  FAIL: SSL certificate verification error.")
            print(f"        This is a local proxy/certificate issue (common on corporate Macs).")
            print(f"        Run this script from the Proxmox LXC instead — it has no proxy.")
            print(f"        Or: curl 'https://api.telegram.org/bot{token}/getMe'")
        else:
            print(f"  FAIL: Network error — {exc.reason}")
            print(f"        Check that api.telegram.org is reachable from this machine.")
        sys.exit(1)


def ok(result: dict) -> bool:
    return bool(result.get("ok"))


# ── Steps ─────────────────────────────────────────────────────────────────────

def step_validate_token(token: str) -> dict:
    print("Step 1 — Validate token")
    result = _api(token, "getMe")
    if not ok(result):
        print(f"  FAIL: {result.get('description', result)}")
        sys.exit(1)
    bot = result["result"]
    print(f"  OK  : @{bot['username']} — {bot['first_name']}")
    return bot


def step_clear_webhook(token: str) -> None:
    print("Step 2 — Clear any stale webhook (long-poll needs this)")
    result = _api(token, "getWebhookInfo")
    if ok(result):
        url = result["result"].get("url", "")
        if url:
            print(f"  Found webhook: {url}")
            del_result = _api(token, "deleteWebhook", {"drop_pending_updates": False})
            if ok(del_result):
                print("  OK  : Webhook deleted.")
            else:
                print(f"  WARN: Could not delete webhook: {del_result}")
        else:
            print("  OK  : No webhook set.")


def step_find_chat(token: str) -> tuple[int, int, str]:
    """Return (chat_id, user_id, username). Requires the user to have messaged the bot."""
    print("Step 3 — Find your chat ID from recent messages")
    print("         (You must have sent at least one message to your bot first.)")

    result = _api(token, "getUpdates", {"limit": 100, "timeout": 0})
    if not ok(result):
        print(f"  FAIL: {result.get('description', result)}")
        sys.exit(1)

    updates = result.get("result", [])
    if not updates:
        print()
        print("  No messages found in getUpdates.")
        print("  → Open Telegram, search for your bot by @username, tap Start,")
        print("    send any message, then re-run this script.")
        sys.exit(1)

    # Find the most recent message from a non-bot user
    for update in reversed(updates):
        msg = update.get("message") or update.get("edited_message")
        if not msg:
            continue
        sender = msg.get("from", {})
        if sender.get("is_bot"):
            continue
        chat_id = msg["chat"]["id"]
        user_id = sender["id"]
        username = sender.get("username") or sender.get("first_name") or str(user_id)
        print(f"  OK  : chat_id={chat_id}  user_id={user_id}  (@{username})")
        return chat_id, user_id, username

    print("  No user messages found. Message your bot first, then re-run.")
    sys.exit(1)


def step_send_hello(token: str, chat_id: int) -> int:
    print("Step 4 — Send Hello, World")
    result = _api(
        token,
        "sendMessage",
        {"chat_id": chat_id, "text": "Hello, World — Prufrock smoke test ✓"},
    )
    if not ok(result):
        print(f"  FAIL: {result.get('description', result)}")
        sys.exit(1)
    msg_id = result["result"]["message_id"]
    print(f"  OK  : message_id={msg_id} delivered.")
    return msg_id


def step_print_env(token: str, user_id: int) -> None:
    print()
    print("=" * 60)
    print("Add these to /opt/prufrock/.env on the Proxmox slice:")
    print("=" * 60)
    print(f"TELEGRAM_BOT_TOKEN={token}")
    print(f"TELEGRAM_USER_ID={user_id}")
    print("=" * 60)


# ── Token discovery ───────────────────────────────────────────────────────────

def _read_dotenv(path: Path) -> dict[str, str]:
    env: dict[str, str] = {}
    if not path.exists():
        return env
    for line in path.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, _, val = line.partition("=")
        env[key.strip()] = val.strip().strip('"').strip("'")
    return env


def resolve_token(cli_token: str | None) -> str:
    if cli_token:
        return cli_token
    # Try environment first
    env_token = os.environ.get("TELEGRAM_BOT_TOKEN")
    if env_token:
        return env_token
    # Try .env file in cwd or parent (the experiment0 root)
    for candidate in [Path(".env"), Path(__file__).parent.parent / ".env"]:
        dotenv = _read_dotenv(candidate)
        if "TELEGRAM_BOT_TOKEN" in dotenv:
            print(f"(Read token from {candidate})")
            return dotenv["TELEGRAM_BOT_TOKEN"]
    print("ERROR: No token found.")
    print("  Provide --token, set TELEGRAM_BOT_TOKEN in env, or add it to .env")
    sys.exit(1)


# ── Entry point ───────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(
        description="Telegram smoke test for Prufrock experiment 0.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--token",
        metavar="BOT_TOKEN",
        default=None,
        help="Bot token from BotFather (overrides env and .env)",
    )
    args = parser.parse_args()

    token = resolve_token(args.token)
    print()

    step_validate_token(token)
    print()
    step_clear_webhook(token)
    print()
    chat_id, user_id, _username = step_find_chat(token)
    print()
    step_send_hello(token, chat_id)
    step_print_env(token, user_id)
    print()
    print("All checks passed. Your Telegram channel is ready for experiment 0.")
    print()
    print("Next: deploy to the Proxmox slice and run `prufrock fire-now`.")


if __name__ == "__main__":
    main()
