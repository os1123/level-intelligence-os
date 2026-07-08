---
llm_canonical: true
title: Level Intelligence OS - Internal Strategy Brief
aliases:
  - Level Agent Native Management System
type: strategy-brief
status: internal
created: 2026-05-18
updated: 2026-05-18
tags:
  - projects
  - construction
  - real-estate
  - level-x
  - operator-intelligence
---

# Level Intelligence OS - Internal Strategy Brief

## Core Read

The right product is not a Mercator clone and not a generic Procore replacement. It is a **Level-specific agent-native operating layer** that starts where Mercator creates value - early market, parcel, permit, relationship, and project signals - then extends into execution workflows that actually govern construction, development, hospitality, finance, and investor decisions.

Mercator's wedge is construction business development intelligence: detect title transfers, rezonings, permits, planning activity, and other early signals; connect those signals to owners, developers, architects, consultants, and GCs; then help BD teams build relationships before projects hit public bid. Level X needs that, but Level also has a broader operating surface because it invests, develops, builds, and manages.

So the strongest pitch is:

> Level X already has the relationships, local judgment, franchise/hospitality experience, development instincts, and construction execution capability. Level Intelligence OS turns those advantages into a repeatable operating system: find opportunities earlier, qualify them consistently, route work to the right people, and coordinate pursuit-to-execution decisions with agents and human approval.

## What Mercator Contributes

Mercator-like capabilities to replicate:

- Early signal ingestion: title transfers, land sales, rezonings, preliminary permits, planning agendas, development news, franchise expansion signals.
- Project graph: parcel, site, owner, developer, architect, engineer, consultant, GC, broker, lender, brand, operator, jurisdiction.
- Opportunity alerts: filtered by market, asset class, size, brand, geography, and Level's prior experience.
- Relationship map: who knows whom, past project history, warm intro paths, contact timing.
- Qualification support: score fit, timing, relationship strength, margin potential, entitlement risk, financing readiness.
- Market intelligence: active developers, brands expanding, competitors, project volume, jurisdiction activity.

Important nuance: Mercator is primarily a **business development intelligence product**. Level Intelligence OS should use that as the upstream wedge, then go beyond it into internal management and execution.

## Internal Framework Patterns

Reusable agentic operating patterns:

- Specialist agents under an orchestrator: opportunity, relationship, permit, bid/RFQ, financial, schedule, investor/reporting.
- Human-in-the-loop authority model: autonomous for research and summaries, suggest for low-risk updates, approval-required for money/schedule/vendor decisions, manual for legal/strategic decisions.
- Audit trail for agent recommendations, human decisions, overrides, and outcomes.
- Bid/RFQ workflow: intake, scope extraction, vendor matching, bid comparison, award routing, contractor notifications.
- Permit workflow: email and portal monitoring, permit status parsing, follow-up drafting, escalation when permits exceed expected review windows.
- Daily/weekly digests: executive pipeline, stalled opportunities, upcoming RFQs, permits at risk, pending approvals.
- Payment/AP extension later: invoice intake, approval routing, QBO/Bill.com style handoff, lien waiver/payment status tracking.

## Level-Specific Fit

Level is not only a GC. Based on the public positioning, Level X combines four verticals: Level Construction, Level Development, Level Hospitality, and Level Capital. Level Construction markets itself as a Chicago and Houston commercial GC/design-build firm with restaurants, retail, franchise interiors, ground-up medical, industrial, and hospitality development experience. Level X's portfolio and history show hotel development, franchise brands, acquisition/repositioning, and capital/investor management.

That means the OS should be designed around **vertical integration**, not just construction projects.

Primary operating domains:

- **Construction BD:** repeat-client commercial work, franchise buildouts, retail, health/wellness, industrial, hospitality.
- **Development:** site selection, entitlement, feasibility, design/planning, development management.
- **Hospitality:** hotel acquisition, renovation, opening, stabilization, guest/asset performance handoff.
- **Capital:** deal sourcing, underwriting, investor reporting, financing milestones.
- **Shared services:** accounting, compliance, vendor/subcontractor records, document control.

## Recommended Product Architecture

### 1. Signal Intelligence Layer

Captures raw market/project signals.

Inputs:

- Permit portals
- Planning commission/city council agendas
- Title transfers and parcel ownership changes
- Zoning applications
- Commercial real estate listings and transactions
- Franchise/brand expansion announcements
- Hospitality acquisition/development news
- Level website/portfolio/client history
- Internal emails, meetings, and documents

Outputs:

- New signal inbox
- Dedupe/entity resolution
- Opportunity candidates
- Account/contact updates
- Watchlist changes
- Weekly market brief

### 2. Opportunity Graph

The central object model should be a graph, not just a table.

Core nodes:

- Opportunity
- Site/parcel
- Account/company
- Contact/person
- Brand/franchise/operator
- Jurisdiction
- Permit/planning event
- RFQ/bid
- Project
- Investor/capital source
- Vendor/subcontractor
- Document
- Task/decision

Core relationships:

- Account owns site
- Contact works at account
- Opportunity occurs at site
- Opportunity involves brand/operator
- Permit belongs to site/opportunity
- RFQ belongs to opportunity/project
- Bid belongs to RFQ
- Investor backs acquisition/development
- Vendor performed on historical project

### 3. Agent Layer

Initial agents:

- **Opportunity Scout:** monitors public/private signals and creates candidate opportunities.
- **Qualification Agent:** scores fit and explains pursue/watch/pass recommendations.
- **Relationship Agent:** generates account briefs, contact maps, warm intro suggestions, and next-touch reminders.
- **Permit/Entitlement Agent:** tracks jurisdiction events, permit status, required documents, and follow-ups.
- **RFQ/Bid Agent:** summarizes RFQs, checks requirements, compares bids, and drafts go/no-go memos.
- **Executive Briefing Agent:** produces weekly pipeline, stuck-decision, risk, and opportunity briefs.
- **Finance/Capital Agent:** later phase for budgets, debt/equity milestones, investor updates, and payment/AP workflows.

Authority model:

- Autonomous: ingest, summarize, classify, score draft, detect duplicates, generate briefs.
- Suggest: update opportunity stage, create tasks, send internal reminders, draft emails.
- Approval-required: external outreach, bid submission, vendor award, budget changes, investor communications.
- Manual: legal commitments, financing decisions, contract execution, final go/no-go on major pursuits.

### 4. Workflow Layer

Use agentic workflow automation:

- Daily signal scan
- New opportunity triage
- Weekly executive pipeline digest
- RFQ intake and extraction
- Bid deadline reminders
- Permit status monitor
- Planning agenda monitor
- Stale relationship reminder
- Go/no-go approval queue
- Procore usage/read-only sync if they use Procore

### 5. Executive Operating View

This is the management product, not just a data product.

Dashboards:

- Top 20 opportunities by score
- High-value relationships needing touch
- Stalled pursuits
- Upcoming bid/RFQ deadlines
- Permit/entitlement blockers
- Pipeline by market, asset class, vertical, and stage
- Development/capital opportunities by underwriting stage
- Workload by internal owner
- Procore cost reduction/readiness if applicable

## MVP Recommendation

Build the first version around **Mercator-like upstream intelligence plus Level-specific pursuit workflow**.

MVP scope:

- Accounts, contacts, opportunities, sites, jurisdictions, RFQs, bids, documents, tasks, notes, activity events, scores.
- Manual import for existing relationship/project data.
- AI opportunity summary and qualification score.
- New signal inbox with sources and dedupe.
- Relationship/account brief.
- RFQ summary and go/no-go memo.
- Executive dashboard and weekly digest.
- Human approval queue for external outreach and bid decisions.

Do not lead with Procore replacement. Lead with earlier opportunity visibility, better pursuit discipline, and executive control. Procore downgrade/replacement should be framed as an evidence-based second-order benefit after usage audit.

## Discovery Questions

Must ask Level:

- Where do new opportunities currently originate: relationships, brands, brokers, municipal signals, inbound RFQs, developers, franchisees, hospitality contacts?
- Who owns opportunity qualification today?
- What is the current go/no-go process?
- Where do RFQs live?
- Which markets are highest priority: Chicago, Houston, Texas broadly, Midwest, national franchise work?
- Which asset classes are highest priority: hospitality, restaurants, retail, medical, industrial, health/wellness, adaptive reuse?
- What tools are currently used: Procore, HubSpot/Salesforce, Excel, Monday, Airtable, SharePoint/Drive, QuickBooks/Sage/NetSuite?
- How many Procore seats/modules are paid for, and who actually uses them?
- What would leadership consider a 90-day win?
- Which internal champions own construction, development, hospitality, capital, and shared services?

## 90-Day Build Thesis

The fastest useful build is:

1. **Weeks 1-2:** data import, role model, opportunity/account/contact schema, executive dashboard skeleton.
2. **Weeks 3-5:** signal inbox, AI summaries, qualification score, relationship briefs, task/next-action workflow.
3. **Weeks 6-8:** RFQ/bid command center, go/no-go memos, approval queue, weekly executive digest.
4. **Weeks 9-12:** permit/planning monitoring, Procore usage audit dashboard, CRM/email/calendar integration, stakeholder training.

Success metrics:

- Leadership can see every active pursuit and next action.
- BD/precon stop relying on scattered spreadsheets/email for pipeline status.
- At least 10 useful opportunities/signals are captured and triaged.
- RFQ deadlines and go/no-go decisions are visible in one place.
- Weekly executive brief is generated from system data.
- Procore downgrade decision is supported by actual usage evidence.

## Pitch Line

> Mercator helps construction firms find the job before it becomes public. Level Intelligence OS goes further: it finds, qualifies, routes, and manages opportunities across Level X's integrated construction, development, hospitality, and capital platform.

## Related

- [[Level Intelligence OS - Codex Handoff - Live Data Prototype]]
- [[Level Intelligence OS Buildout Plan]]
- [[Level Intelligence OS - Strategic Dossier]]
- [[Level Intelligence OS - Agentic Architecture Blueprint]]
- [[Level Intelligence OS - ROI and Compounding Value Model]]
- [[Level Intelligence OS - Implementation and Discovery Plan]]

## Sources

- [Mercator.ai - A Guide to Construction Project Intelligence](https://www.mercator.ai/articles/construction-project-intelligence-tips)
- [Mercator.ai - What is a Building Project Intelligence Platform?](https://www.mercator.ai/articles/construction-intelligence-platform-guide)
- [Level Construction](https://www.levelconstruction.net/)
- [Level Construction About](https://www.levelconstruction.net/about)
- [Level X Group - Who We Are](https://levelxgroup.net/who-we-are/)
- [Level X Group - Companies](https://levelxgroup.net/companies/)
- [Level X Group - Portfolio](https://levelxgroup.net/portfolio/)
