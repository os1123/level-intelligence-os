---
llm_canonical: true
title: Level Intelligence OS - Codex Handoff - Live Data Prototype
aliases:
  - Level OS Live Data Handoff
  - Level OS Codex Build Brief
type: build-handoff
status: ready-for-build
created: 2026-07-07
updated: 2026-07-07
tags:
  - projects
  - level-x
  - construction
  - operator-intelligence
  - build
  - codex
---

# Level Intelligence OS - Codex Handoff - Live Data Prototype

> **For:** Codex (implementation agent)
> **Goal:** Turn the seeded click-through mockup into a working prototype that pulls **real Chicago restaurant & retail building permits** and scores them, without changing the existing UI.
> **Context for the meeting:** This is the "it actually works" artifact. The demo wedge is Chicago restaurant/retail buildouts; the strategic story is a proprietary, fused, daily-growing intelligence repository. See [[Level Intelligence OS - Internal Strategy Brief]] and [[Level Intelligence OS - One Page Dossier and Term Sheet]].

## Current State (what exists today)

- **`level-intelligence-os-demo.html`** — a single self-contained clickable mockup (vanilla JS + inline CSS, no build step). It renders five layers: Signal Inbox, Opportunity Pipeline, Executive Brief, Alerts, plus a **Fused Intelligence** panel per opportunity and an **Intelligence Repository** moat view.
- **All data is seeded/hardcoded** in the `OPPS` array and `ENRICH` map inside the file's `<script>`. Nothing calls any API. The repository counters (e.g. "214 days of history", "48,240 permits") are fabricated for visual effect.
- The UI, styling, and view logic are good and should be **preserved**. This task replaces the *data layer* only.

## Objective

Make the **Signal Inbox + Opportunity detail (score + reasoning)** run on **live City of Chicago permit data**. Keep everything else (pipeline, brief, alerts, graph, enrichment panel) rendering off the same live records where possible; where a layer needs sources we haven't wired yet, leave it clearly labeled as roadmap (see Guardrails).

## Recommended Architecture (keep it simple for a demo)

Do **not** stand up a live server for the meeting. Use a **build step** that fetches + scores, writes a static JSON, and let the page load that JSON. This avoids CORS issues, keeps the Anthropic API key server-side (never in the browser), and makes "refresh the data" a single command.

```
scripts/
  fetch-and-score.mjs     # Node 20+, run manually to refresh
data/
  permits.json            # generated output the page reads
level-intelligence-os-demo.html   # modify: load data/permits.json instead of hardcoded OPPS
.env                      # ANTHROPIC_API_KEY, CHICAGO_APP_TOKEN (optional)
```

Flow: `node scripts/fetch-and-score.mjs` → pulls Chicago permits → filters to restaurant/retail → LLM scores each → writes `data/permits.json`. The HTML `fetch('data/permits.json')` on load and renders with the existing functions.

### Step 1 — Fetch (Chicago Building Permits API)

- **Endpoint:** `https://data.cityofchicago.org/resource/ydr8-5enu.json` (Socrata SODA v2, SoQL query params).
- **No key required** for low volume; register a free **app token** for higher limits and pass it as the `X-App-Token` header. Put it in `.env` as `CHICAGO_APP_TOKEN` (optional).
- **Query:** recent records, restaurant/retail-relevant, ordered by newest.
  - `$where`: `issue_date > '2026-01-01T00:00:00'` (or rolling last N days) AND `reported_cost > 100000`.
  - Restaurant/retail is **not a native field** — filter on `permit_type` in `{PERMIT - NEW CONSTRUCTION, PERMIT - RENOVATION/ALTERATION}` and keyword-match `work_description` for: `restaurant, kitchen, hood, cafe, bar, tenant, build-out, buildout, retail, food, dining`. Do the keyword filter in code after fetch (SoQL `like` is limited).
  - `$order`: `issue_date DESC`, `$limit`: 200 (then trim to top ~15 for the demo).
- **Fields to keep:** `id`, `permit_`, `permit_type`, `work_description`, `street_number`, `street_direction_name`/`street_name`, `reported_cost`, `total_fee`, `application_start_date`, `issue_date`, `community_area`, `ward`, `latitude`, `longitude`, and any `contact_*`/`contractor` fields present.
- **Normalize** each into the shape the UI already expects (mirror the existing `OPPS` object: `id, addr, hood, type, score, rec, cost, sqft, filed, status, desc, owner, brand, contractor, arch, reasons[], actions[], tl[]`). Map `community_area` → neighborhood label; derive `addr` from street parts; `cost` from `reported_cost`.

### Step 2 — Score (LLM, Anthropic SDK)

- Use the Anthropic SDK (`@anthropic-ai/sdk`), model **`claude-opus-4-8`** (or `claude-sonnet-5` for cheaper/faster iteration). Key from `.env` as `ANTHROPIC_API_KEY`. Verify current model IDs/params against the `claude-api` skill before writing the call.
- For each normalized permit, one tool-use / structured-output call returning:
  ```json
  { "score": 0-100, "rec": "pursue|watch|pass",
    "reasons": [ { "d": "up|dn|nu", "t": "one-sentence rationale (may include <b>…</b>)" } ] }
  ```
- **Scoring rubric** (put in a `RUBRIC` const so it's tunable — this encodes Level's judgment):
  - Asset-class fit: full-service restaurant / fast-casual / retail buildout = high; office/amenity café = low.
  - Deal-size band: sweet spot **$800K–$2M reported cost**; below ~$250K down-weight.
  - Geography: **West Loop, Fulton Market, River North** = Level's dense sub cluster, up-weight; outer neighborhoods slightly down.
  - **No GC named on the permit** = open pursuit window, up-weight.
  - Repeat/known developer or franchise signal = up-weight.
- Keep reasons **explainable and specific** — reference the actual permit fields, matching the tone of the current seeded reasons.

### Step 3 — Wire the page

- Replace the hardcoded `const OPPS = [...]` with `let OPPS = []` and a loader: `fetch('data/permits.json').then(...).then(data => { OPPS = data; renderInbox(); })`.
- Everything downstream (inbox cards, detail, pipeline, brief) already reads from `OPPS` — no other rendering changes needed.
- Recompute the derived numbers in the Executive Brief and Repository view from the real array length instead of hardcoded totals.

## Guardrails (keep it honest — this matters for the room)

1. **Enrichment / Fused Intelligence panel is roadmap, not live.** Foot traffic, liquor-license timing, co-tenancy, and the "derived insight" require sources we haven't wired. Either (a) keep the `ENRICH` panel but add a visible `Illustrative — roadmap layer` tag, or (b) generate a *lighter* real insight from permit fields only and label the richer fusion as Phase 2. **Do not present fabricated enrichment as live.**
2. **The "history / moat" counters must be truthful.** Replace "214 days of history / 48,240 captured" with real computed values from this run (e.g. "N permits captured today; daily capture begins <date>"). The time-series moat is real *going forward* — frame it as beginning now, not already accumulated.
3. **Never put `ANTHROPIC_API_KEY` in the client.** Scoring happens only in the build script.
4. Keep the existing "seeded sample" footers accurate — flip them to "live" only for the layers that are actually live.

## Acceptance Criteria

- [ ] `node scripts/fetch-and-score.mjs` pulls real Chicago permits and writes `data/permits.json` with ≥10 restaurant/retail records.
- [ ] Opening `level-intelligence-os-demo.html` shows those **real permits** in the Signal Inbox, each with an LLM score + explainable reasons on the detail page.
- [ ] Addresses/costs are verifiable against the City of Chicago portal.
- [ ] Enrichment and repository counters are either truthfully computed or clearly labeled roadmap/illustrative.
- [ ] No API keys in the HTML or committed to the repo; `.env` is gitignored.
- [ ] Re-running the script refreshes the data with no code changes.

## Out of Scope (for this pass)

- Live liquor-license / business-license / Maps / weather enrichment (Phase 2 — the real moat build).
- Any hosted backend or auth.
- Pipeline drag-and-drop, alert rule editing, relationship/RFQ/Procore/Capital modules.

## Nice-to-Have (only if time)

- A tiny "Refresh" affordance in the UI header that re-fetches `data/permits.json`.
- Persist each run's `permits.json` to `data/history/<date>.json` — the literal first brick of the time-series moat.

## Related

- [[Level Intelligence OS - Internal Strategy Brief]]
- [[Level Intelligence OS - One Page Dossier and Term Sheet]]
- [[Level Intelligence OS - Agentic Architecture Blueprint]]
- [[Level Intelligence OS - ROI and Compounding Value Model]]
- [[Level Intelligence OS - Official Package Index]]
