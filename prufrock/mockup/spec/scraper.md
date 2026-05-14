# Spec: Public-Domain Poem Corpus for "Last Two Lines" Exquisite Corpse

## 1. Goal

Build a local-first ingestion system that collects public-domain poems, extracts clean poem text, stores metadata and final two-line prompts, and exposes them for a project where poets write responses to the final two lines of existing poems.

Core principle: prefer APIs, bulk catalogs, and downloadable datasets over scraping HTML pages. Project Gutenberg explicitly asks developers to use its RDF/XML/CSV metadata rather than crawling the site.

## 2. Legal/public-domain policy

"Public domain globally" is not a single fixed category. Copyright terms differ by jurisdiction. Treat "globally public domain" as a conservative computed status, not a source claim.

Use a three-tier rights model:

| Status | Use |
|---|---|
| global_pd_confident | Author died ≥100 years ago, publication is pre-1929, no modern translation/editorial claim, source marks PD/CC0 |
| source_pd_only | Public domain in source jurisdiction, e.g. US public domain, but not globally guaranteed |
| needs_review | Translation, anthology, uncertain author date, modern edition, unclear license |

For poet-facing prompts, only use global_pd_confident unless explicitly running a jurisdiction-limited edition.

Standard Ebooks works from US-public-domain texts and dedicates its own ebook files to CC0/public domain, but its collection policy is US-public-domain-focused, not global-public-domain-focused.

## 3. Source priority

### Phase 1: easiest/highest confidence

1. **Project Gutenberg**
   * Use RDF catalog / CSV / Gutendex-style local API.
   * Do not crawl pages.
   * Filter by bookshelf=Poetry, language, author dates, and text/plain availability.
   * Gutendex is useful for prototyping, but its own docs recommend self-hosting for long-term use.

2. **Gutenberg Poetry Corpus**
   * Excellent bootstrap dataset: about 3.08M poetry lines from 1,191 Gutenberg IDs.
   * Weakness: line corpus, not necessarily reliable poem boundaries.
   * Use for line-level experiments, not canonical poem records unless reconciled back to source books.

3. **Standard Ebooks**
   * Use OPDS feeds, not page scraping; Standard Ebooks publishes OPDS ebook feeds.
   * High text quality, but mostly book-level works. Need poem extraction from EPUB XHTML.

### Phase 2: broader coverage

4. **Wikisource**
   * Use MediaWiki Action API, not HTML scraping. MediaWiki's Action API is the official mechanism.
   * Useful for individual poem pages and multilingual material.
   * Requires stronger rights and translation checks.

5. **Internet Archive**
   * Use Search/Metadata APIs and item files rather than crawling. IA provides developer APIs including metadata and Python tooling.
   * OCR quality and rights metadata vary. Good as enrichment, not first source.

6. **HathiTrust**
   * Useful for bibliographic rights/volume metadata; bulk work should use OAI or HathiFiles, not the Bibliographic API, which is intended for small numbers of items.

## 4. Recommended stack

Use Python for ingestion and text processing.

Best mechanism for an AI agent:

* Typer for CLI commands.
* httpx for API/download requests.
* pydantic for typed source records.
* BeautifulSoup/lxml for XHTML/EPUB parsing.
* ebooklib for EPUB unpacking.
* rdflib for Gutenberg RDF if parsing directly.
* sqlite + SQLModel/SQLAlchemy locally.
* PostgreSQL later.
* DuckDB optional for analysis/export.
* ruff + pytest for agent-safe iteration.
* Playwright only as a last resort; most target sources have APIs/catalogs.

Avoid building the agent around browser scraping. Give it source adapters with explicit contracts.

## 5. Local-first architecture

```
poem-corpus/
  pyproject.toml
  .env.example
  data/
    raw/
      gutenberg/
      standard_ebooks/
      wikisource/
    processed/
    exports/
  corpus/
    sources/
      gutenberg.py
      standard_ebooks.py
      wikisource.py
      internet_archive.py
    extract/
      epub.py
      plain_text.py
      poem_segmentation.py
      last_lines.py
    rights/
      public_domain.py
    db/
      models.py
      migrations/
    cli.py
```

CLI commands:

```
poemcorpus init-db
poemcorpus ingest gutenberg --language en --limit 100
poemcorpus ingest standard-ebooks --limit 50
poemcorpus process pending
poemcorpus review queue
poemcorpus export prompts --format jsonl
```

## 6. Data model

Minimum tables:

**sources**
- id, name, base_url, access_method (api | bulk | opds | dataset), terms_url, notes

**works**
- id, source_id, source_work_id, title, author_name, author_birth_year, author_death_year, language, publication_year, source_rights_statement, computed_rights_status, rights_confidence, source_url, canonical_url, raw_file_path, created_at, updated_at

**poems**
- id, work_id, title, sequence_index, text_clean, line_count, first_line, last_line, penultimate_line, last_two_lines, extraction_method, extraction_confidence, needs_human_review

**poem_lines**
- id, poem_id, line_number, text

**prompts**
- id, poem_id, prompt_text, prompt_type (last_two_lines), status (active | held | retired), created_at

**responses**
- id, prompt_id, poet_name, response_text, submitted_at, publication_status, consent_license

Store raw files separately on disk locally, later in S3-compatible object storage.

## 7. Poem extraction rules

### Plain text books

1. Strip source boilerplate.
2. Detect title/author blocks.
3. Preserve line breaks.
4. Split poems using headings, all-caps titles, table-of-contents anchors, or repeated blank-line structures.
5. Reject fragments under 4 lines unless source page is clearly a short poem.

### EPUB books

1. Unpack EPUB.
2. Parse content.opf for spine order.
3. Extract XHTML body text.
4. Preserve `<p>`, `<br>`, `<div class="verse">`, `<span class="i1">` style lineation.
5. Ignore notes, copyright pages, ToC, indexes.

### Last-two-line rule

For each poem:

* Normalize Unicode.
* Remove empty lines.
* Exclude title, epigraph, footnotes.
* Preserve original punctuation.
* Store:
  * penultimate_line
  * last_line
  * last_two_lines = penultimate + "\n" + last

Flag for review if:

* Last line is a page number.
* Last line is footnote marker-heavy.
* Poem has fewer than 4 meaningful lines.
* Final lines are editorial notes.
* Text is a translation after 1925.
* Author death year missing.

## 8. Rights computation

```python
def compute_rights(author_death_year, publication_year, source_license, translator_death_year=None):
    if source_license in {"CC0", "Public Domain Mark"}:
        source_ok = True
    else:
        source_ok = False
    if author_death_year and author_death_year <= current_year - 100:
        author_ok = True
    else:
        author_ok = False
    if publication_year and publication_year <= 1928:
        publication_ok = True
    else:
        publication_ok = False
    if translator_death_year and translator_death_year > current_year - 100:
        return "needs_review"
    if author_ok and publication_ok and source_ok:
        return "global_pd_confident"
    if publication_ok and source_ok:
        return "source_pd_only"
    return "needs_review"
```

Use 100 years post mortem auctoris as the conservative "global" threshold. This is stricter than many jurisdictions, but safer for an international project.

## 9. AI-agent workflow

The AI agent should not "browse and scrape freely." It should operate through tools:

```
SourceAdapter
- discover()
- fetch_metadata()
- fetch_text()
- parse()
- normalize()
- compute_rights()
- store()
```

Each adapter returns a typed object:

```python
class SourceWork(BaseModel):
    source: str
    source_work_id: str
    title: str
    authors: list[Author]
    language: str | None
    publication_year: int | None
    rights_statement: str | None
    download_urls: list[str]
    source_url: str
```

Agent guardrails:

* Never ingest a source without a source adapter.
* Never mark global public domain from source text alone.
* Never overwrite manually reviewed rights.
* Log every download URL and timestamp.
* Keep raw input immutable.

## 10. Quality controls

Automated checks:

* duplicate text hash
* duplicate title/author
* suspiciously long "poems"
* OCR garbage score
* language detection mismatch
* missing author death date
* final-line anomaly detection

Human review queue should show:

* Title, Author, Author dates, Publication year, Source
* Rights status
* Extracted poem text
* Last two lines
* Reason for review
* Approve / Edit / Reject

## 11. Deployment path

### Local MVP

* SQLite
* filesystem raw storage
* Typer CLI
* JSONL exports
* manual review via simple Streamlit or Flask admin

### Small hosted version

* PostgreSQL
* S3-compatible object storage
* FastAPI API
* background jobs with Dramatiq/RQ
* admin UI for review
* nightly source refresh jobs

### Larger-scale version

* Postgres + pgvector for similarity/de-duplication
* S3 object storage
* Kubernetes or ECS workers
* queue-based ingestion
* separate read API for poem prompts
* provenance dashboard
* versioned corpus releases

## 12. API endpoints (later)

```
GET /prompts/random?language=en&rights=global_pd_confident
GET /poems/{id}
POST /responses
GET /sources
GET /admin/review-queue
POST /admin/poems/{id}/approve
POST /admin/poems/{id}/reject
```

## 13. MVP acceptance criteria

The first working version is successful when it can:

1. Ingest 100+ candidate poetry works from Project Gutenberg without crawling HTML.
2. Extract at least 500 poem candidates.
3. Compute conservative rights status.
4. Store raw files, metadata, poem text, and last-two-line prompts.
5. Export approved prompts as JSONL.
6. Provide a review queue for uncertain poems.
7. Re-run idempotently without duplicating records.

## 14. Recommended first build order

1. Build SQLite schema.
2. Implement Project Gutenberg adapter from RDF/Gutendex/local metadata.
3. Fetch plain text files.
4. Strip boilerplate.
5. Segment poems conservatively.
6. Extract last two lines.
7. Add rights computation.
8. Add review queue.
9. Add Standard Ebooks EPUB adapter.
10. Add Wikisource later.
