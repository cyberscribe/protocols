# Workshop takeaway card

A double-sided plastic card handed out at the end of the workshop:

- **Side A** — Distributed cognition in AI-enabled teams (the executive-function diagram).
- **Side B** — DRIVE.

Both sides light mode, portrait, A4-derived artwork.

## Status

Both sides are built. `handout-card_a4.pdf` is the two-page light render — page 1 side A, page 2
side B — generated from `handout-card_a4.html`.

Side A is unchanged. `exec-fn-portrait.py` generates the portrait transposition in both themes
from one source; the palette is CSS custom properties, so `render(theme='light')` is the whole of
the light-mode switch.

Side B is `build-drive-card.py`: the slide-11 layout ported, not a new drawing. Five lettered
circles down the left as bullets, phase name beside each and the descriptor beneath, copy taken
verbatim from `peakepro-diagnostics/go-to-market/video-trust-trap-research/4x5/deck-4x5.pptx`.
Same shape as side A — palette dicts per theme, a `build()` returning the elements, a
`render(theme)` wrapper, the same 1040x1290 frame — so the two sides register when the card is
flipped, and the deck and the handout can share a source.

**The circle colours are the deck's five, and they are not the six content-type colours.** Slide
11 uses `5C90F0 3FBFAE E8A33D D9718F 5ECB92`; three of those are already spoken for on side A
(project reference, templates, projects). Side B carries no content types, so nothing is
mis-keyed — but the earlier note below about keeping six colours identical across both sides only
governs side A now. If the two palettes should be reconciled, that is a deck change first.

On light the deck values are darkened to `2D70EC 2B8276 A46A13 CD456C 2B8656`, holding hue and
saturation and dropping lightness until white letters clear 4.5:1. The deck values sit at
2.0–3.1:1 on white, which is fine on the dark slide and not fine on a white card reduced from A4.

Rendering: `python3 build-drive-card.py` writes both SVGs; the PDF is Chromium headless
`--print-to-pdf` over `handout-card_a4.html`. That HTML links Google Fonts, so the render host
needs network or Poppins and JetBrains Mono installed locally, or the type falls back and the
proof is not representative.

## Print notes

- Card stock is plastic, so the light palette needs checking against a real proof: the pale card
  fills (`#F4F7FC`, `#F7F9FD`) may disappear against white plastic. Consider dropping the fills
  and keeping only the strokes and the colour keys.
- The copyright line reads "© 2026 ROBERT PEAKE · ROBERTPEAKE.COM" and is a placeholder. Confirm
  the entity before anything goes to print.
- Keep the six content-type colours identical across both sides: they are the whole reason the
  two diagrams belong on one card.
