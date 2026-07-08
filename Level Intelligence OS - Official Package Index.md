---
llm_canonical: true
title: Level Intelligence OS - Official Package Index
aliases:
  - Level Intelligence OS Official Package
  - Level OS Client Package
type: client-package-index
status: draft
created: 2026-05-26
updated: 2026-07-07
tags:
  - projects
  - level-x
  - construction
  - operator-intelligence
  - proposal
  - deck
---

# Level Intelligence OS - Official Package Index

## Package Location

Official exports live here:

`/Users/omar/Grounded/Projects/Level Intelligence OS/official`

The redone one-pager and comprehensive Word packet are generated from:

`scripts/redo_official_docs.py`

## Client-Ready Files

### One-Page Dossier

- PDF: `official/Level Intelligence OS - Official One Pager.pdf`
- DOCX: `official/Level Intelligence OS - Official One Pager.docx`
- HTML: `official/index.html`

Purpose: short executive overview with pain points, outcomes-not-code framing, system areas, Procore-first strategy, 90-day pilot, and term sheet skeleton.

### Official Dossier

- PDF: `official/Level Intelligence OS - Official Dossier.pdf`
- DOCX: `official/Level Intelligence OS - Official Dossier.docx`
- HTML: `official/dossier.html`

Purpose: longer client-ready proposal with executive summary, business problem, outcomes framing, Procore-first strategy, reusable infrastructure patterns, operating system areas, pilot, ownership, and commercial principles.

### Comprehensive Client Packet

- PDF: `official/Level Intelligence OS - Comprehensive Client Packet.pdf`
- DOCX: `official/Level Intelligence OS - Comprehensive Client Packet.docx`
- HTML: `official/comprehensive-packet.html`

Purpose: full client packet with detailed proposition, pain narrative, built-for-Level positioning, reusable infrastructure patterns, Procore bridge strategy, market-shift framing, operating modules, agentic structure, ROI/value model, pilot, phase-two expansion, ownership/trust terms, and discovery agenda.

### Executive Slide Deck

- PDF: `official/Level Intelligence OS - Executive Slide Deck.pdf`
- HTML: `official/slides.html`

Purpose: browser-native slide deck and PDF deck for presenting the proposal. The deck is structured around pain, category context, why now, reusable infrastructure, Procore bridge strategy, market shift, outcomes-not-code, product surfaces, ROI, pilot, ownership, and close.

### Package Landing Page

- HTML: `official/package.html`

Purpose: local index page linking the one-page HTML, dossier HTML, slide HTML, and PDF exports.

## Interactive Demo & Prototype

Added 2026-07-07 to support the scoping meeting — proving the concept is real and demo-able on a niched-down 30-day slice.

### Clickable Demo (seeded)

- HTML: `level-intelligence-os-demo.html`

Purpose: self-contained click-through mockup of the **Chicago restaurant & retail buildout** wedge, threading all five layers (Signal Inbox → Opportunity Graph → Qualification → Workflow → Executive Brief) plus a **Fused Intelligence** panel and an **Intelligence Repository** moat view. Runs offline. **All data is seeded/hardcoded — not live.** This is the "looks finished" artifact for the room.

### Data-Sourcing Answer

For "where does the permit data come from?": the Chicago demo runs on the **City of Chicago Building Permits open API** (Socrata/SODA, `data.cityofchicago.org/resource/ydr8-5enu`) — official, free, no scraping. Scaling beyond Chicago uses commercial aggregators or targeted scraping behind a source-agnostic ingestion layer. The moat is the fused, daily-captured, outcome-labeled repository, not the raw feed.

### Live-Data Build Handoff

- Note: [[Level Intelligence OS - Codex Handoff - Live Data Prototype]]

Purpose: build brief for Codex to turn the seeded mockup into a working prototype pulling **real** Chicago permits (fetch → LLM score → static JSON → same UI), with honest guardrails on enrichment and the history/moat framing. Status: ready-for-build.

## Hosting Recommendation

For review with Level, use a static host:

1. **Vercel** - best if we want a polished, shareable URL quickly and may update the HTML deck.
2. **Netlify Drop** - fastest low-friction static publish if we only need to drag-and-drop the `official` folder.
3. **GitHub Pages** - fine for a durable archive, but slower if this is just a client preview.
4. **PDF only** - safest for formal sending, especially before the web version is final.

Recommended path: send the PDF one-pager and PDF slide deck first; host the HTML deck only after one final copy/design pass.

## Related

- [[Level Intelligence OS - Codex Handoff - Live Data Prototype]]
- [[Level Intelligence OS - One Page Dossier and Term Sheet]]
- [[Level Intelligence OS - Detailed Proposition]]
- [[Level Intelligence OS - Slide Deck Plan]]
- [[Level Intelligence OS - Website and HTML Deck Content]]
- [[Level Intelligence OS - Strategic Dossier]]
- [[Level Intelligence OS - ROI and Compounding Value Model]]
