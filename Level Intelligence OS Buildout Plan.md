---
llm_canonical: true
title: Level Intelligence OS Buildout Plan
aliases:
  - Level X Intelligence OS
  - Level Operator Intelligence Layer
type: project-plan
status: draft
created: 2026-05-18
updated: 2026-05-18
tags:
  - projects
  - construction
  - real-estate
  - operator-intelligence
---

# Level Intelligence OS Buildout Plan

## Positioning

Level X should not be pitched a generic SaaS dashboard. The stronger framing is an **operator intelligence layer** for a vertically integrated real estate, construction, hospitality, capital, and development organization.

Core thesis:

> Level X already has the relationships, construction judgment, hospitality/development experience, and local market instincts. Level Intelligence OS turns that institutional knowledge into a repeatable operating system for sourcing, qualifying, pursuing, and executing opportunities.

Working product name:

**Level Intelligence OS**

Primary promise:

- Find and qualify opportunities across hospitality, retail, development, franchise, construction, and adaptive reuse.
- Track entitlement, preconstruction, RFQs, bids, and owner/developer relationships.
- Give executives one operating view across active pursuits, pending decisions, risks, and next actions.
- Reduce dependency on expensive construction software where Level X does not need full enterprise project-management depth.

## Product Structure

### 1. Opportunity Intelligence

Purpose: capture potential projects before they become formal jobs.

Core objects:

- Opportunity
- Site / parcel / address
- Account / owner / developer / brand
- Contact
- Market
- Asset type
- Lead source
- Internal owner
- Qualification status
- Next action
- Pursuit stage

Primary views:

- Opportunity pipeline
- Market map
- New signals inbox
- High-priority opportunities
- Watchlist
- Passed opportunities with reasons

Example opportunity types:

- Hotel development
- Retail pad / center development
- Restaurant / franchise buildout
- Adaptive reuse
- Mixed-use development
- Capital-backed acquisition or repositioning
- Municipal / public-private opportunity
- Repeat-owner construction opportunity

### 2. Qualification Engine

Purpose: convert Level X's judgment into a repeatable scoring system.

Score dimensions:

- Geography fit
- Asset type fit
- Project size
- Timeline fit
- Relationship strength
- Entitlement complexity
- Financing / capital fit
- Construction margin potential
- Level X prior experience match
- Competitive risk
- Strategic value

Outputs:

- Pursue / Watch / Pass
- Confidence score
- Reasoning summary
- Key risks
- Recommended next action
- Similar historical projects
- Suggested internal owner

The scoring should remain editable by humans. AI should explain and assist, not silently dictate.

### 3. Relationship Intelligence

Purpose: make scattered institutional knowledge usable by the org.

Track:

- Owners
- Developers
- Brokers
- Architects
- Lenders
- Franchise groups
- Hotel operators
- Municipal contacts
- Subcontractors
- Consultants

Features:

- Account timelines
- Last touch / next touch
- Relationship owner
- Warm intro paths
- Past project history
- Open opportunities by account
- AI-generated account brief
- Notes from calls, emails, and meetings

### 4. Entitlement + Preconstruction Tracker

Purpose: track early project risk before full construction operations begin.

Objects:

- Jurisdiction
- Entitlement milestone
- Permit
- Planning meeting
- Precon task
- RFI / clarification
- Design document
- Deadline

Features:

- Jurisdiction notes
- Planning commission / city council dates
- Permit status
- Required documents
- Risk flags
- Responsible person
- Timeline view
- Deadline reminders

### 5. Bid / RFQ Command Center

Purpose: coordinate RFQs and bid responses without everything living in email.

Features:

- RFQ intake
- Bid deadline calendar
- Go / no-go decision record
- Scope summary
- Required attachments checklist
- Internal assignment
- Document links
- Clarification questions
- Bid status
- Win/loss outcome
- Comparable prior bids
- Subcontractor/vendor lists

AI support:

- RFQ summary
- Key requirements extraction
- Missing document detection
- Draft go/no-go memo
- Similar project matching
- Risk summary

### 6. Executive Dashboard

Purpose: give leadership a high-signal operating view.

Dashboards:

- Active pursuits
- Top scored opportunities
- Upcoming bid/RFQ deadlines
- Stalled opportunities
- Pipeline value by stage
- Market heatmap
- Win/loss reasons
- Relationship activity
- Team workload
- Jurisdiction deadline calendar
- Procore replacement/downgrade readiness

## Recommended Stack

### Core Application

- **Next.js** for the web application.
- **Supabase Postgres** for the primary database.
- **Supabase Auth** for login and baseline role-based access.
- **Supabase Row Level Security** for permission boundaries.
- **Supabase Storage** for documents, RFQs, plans, and attachments.
- **Vercel** for hosting.
- **Trigger.dev, Inngest, or Supabase Edge Functions** for background jobs.
- **Sentry** for error tracking.
- **PostHog** for product usage analytics if needed.

### Enterprise Access

- **WorkOS, Auth0, Clerk Enterprise, or Microsoft Entra ID** for SSO/SAML if Level X requires enterprise login.
- Role-based access for executive, BD, preconstruction, estimating, construction ops, finance, and admin.
- Audit logs for key changes.
- Environment separation: dev, staging, production.
- Backup/export strategy for data portability.

### AI Layer

Use AI for extraction and summarization first, then scoring and recommendation.

Capabilities:

- Summarize RFQs, permits, planning agendas, and emails.
- Extract dates, locations, counterparties, and requirements.
- Generate account briefs.
- Suggest qualification score with explanation.
- Draft go/no-go memos.
- Identify missing bid documents.
- Answer questions over opportunities, contacts, RFQs, and project history.

Likely model options:

- OpenAI / Claude / Gemini for extraction, summarization, and reasoning.
- Embeddings/vector search for document and historical project retrieval.
- Supabase pgvector or a managed vector DB if scale requires it.

## Data Model

Initial tables:

- organizations
- users
- roles
- teams
- accounts
- contacts
- opportunities
- sites
- markets
- jurisdictions
- permits
- planning_events
- rfqs
- bids
- documents
- tasks
- notes
- activity_events
- scores
- integrations
- audit_logs

Important relationships:

- Account has many contacts.
- Account has many opportunities.
- Opportunity may have one or more sites.
- Opportunity has many notes, tasks, documents, scores, and activity events.
- RFQ belongs to an opportunity or project.
- Bid belongs to an RFQ.
- Jurisdiction links to sites, permits, and planning events.

## Integrations And APIs

### Highest Value

1. **Google Workspace / Microsoft 365**
   - Email ingestion
   - Calendar deadlines
   - Drive / SharePoint document links
   - Contact extraction
   - Meeting notes

2. **CRM**
   - HubSpot or Salesforce if already in use
   - Sync accounts, contacts, opportunities, and activities
   - Avoid forcing a CRM migration at first

3. **Maps + Parcel Data**
   - Google Maps or Mapbox
   - Regrid, LightBox, CoreLogic, county assessor data, or local parcel APIs depending budget
   - Site context, ownership, parcels, zoning, and proximity analysis

4. **Permit / Planning Data**
   - City/county permit portals
   - Planning commission agendas
   - Accela-style municipal systems where accessible
   - Public meeting agendas and PDFs

5. **News / Web Monitoring**
   - Exa, Tavily, SerpAPI, Google alerts replacement, or custom crawlers
   - Hospitality development news
   - Retail expansion signals
   - Franchise announcements
   - Local development press

6. **Document AI**
   - PDF extraction
   - OCR for scanned packets
   - RFQ classification
   - Bid document checklisting
   - Summary and risk extraction

7. **Slack / Microsoft Teams**
   - Opportunity alerts
   - Bid deadline reminders
   - Approval prompts
   - Daily/weekly digest

### Construction System Integrations

If Level X uses Procore today, do not rip it out on day one. Integrate first, observe actual usage, then downgrade or replace modules selectively.

Potential construction connectors:

- Procore API for project data, RFIs, submittals, drawings, directories, commitments, and observations.
- Autodesk Construction Cloud if they use it.
- Bluebeam for drawings/reviews if relevant.
- QuickBooks, Sage, NetSuite, or other ERP/accounting systems if financial handoff matters.

## Large Organization Availability Model

Deployment:

- Custom domain such as intelligence.levelx.com.
- SSO/SAML login.
- Mobile-responsive web app.
- Teams/Slack notifications.
- Email digest for non-daily users.
- Admin console for user/role management.

Access model:

- Executive: read dashboards, key decisions, risks, pipeline.
- Business Development: manage opportunities, accounts, contacts, activities.
- Preconstruction: manage RFQs, scope, bid checklist, go/no-go support.
- Estimating: bid package tracking, deadlines, notes, vendor/subcontractor lists.
- Construction Ops: project handoff, status visibility, selected Procore replacement modules.
- Finance / Capital: pipeline, budgets, returns, financing notes.
- Admin: integrations, permissions, audit logs, data imports.

Permission boundaries:

- Org-wide admin.
- Team/region access.
- Project-specific access.
- Private executive notes if required.
- Audit trail for stage, score, decision, owner, and financial changes.

Adoption path:

- Start with leadership + BD + precon.
- Add estimating after RFQ workflow is stable.
- Add construction operations only after Procore module audit is complete.
- Keep CSV import/export available so the system does not feel like a lock-in trap.

## Procore Exit / Downgrade Feasibility

### Short Answer

**Yes, moving away from Procore may be feasible, but only if Level X does not depend deeply on Procore for field execution, drawings, RFIs, submittals, change orders, commitments, daily logs, financial controls, and subcontractor collaboration.**

The safer recommendation is:

1. Build Level Intelligence OS around opportunity, pursuit, precon, and executive visibility first.
2. Integrate with Procore while measuring actual module usage.
3. Replace or downgrade low-risk Procore modules first.
4. Keep Procore only where it is genuinely needed for field execution, compliance, or subcontractor coordination.

The migration strategy should be **part-by-part replacement**, not a full rip-and-replace. Each module should earn replacement independently by proving it is cheaper, simpler, and safer inside Level Intelligence OS than inside Procore.

Replacement principle:

- Replace upstream intelligence first.
- Replace reporting and visibility second.
- Replace coordination workflows third.
- Replace field execution modules only after workflow, legal, subcontractor, and data-retention requirements are clear.
- Keep any Procore module that is still cheaper to rent than to rebuild and maintain.

### Why Full Replacement Is Risky

Procore is expensive, but it is also sticky because it often becomes the operational record for:

- Drawings
- RFIs
- Submittals
- Daily logs
- Change events
- Commitments
- Punch lists
- Observations
- Budget changes
- Subcontractor collaboration
- Owner-facing construction documentation

Replacing all of that with a custom system is possible, but it can become a large construction operations product rather than an intelligence OS. That may be worth it eventually, but it should not be the first wedge.

### Where Replacement Is Most Feasible

Good candidates to replace or pull out of Procore:

- Early opportunity tracking
- Business development pipeline
- Preconstruction pursuit tracking
- RFQ intake and go/no-go decisions
- Executive dashboards
- Relationship/account intelligence
- Market intelligence
- Planning/permit signal monitoring
- Internal notes and qualification scoring
- Weekly leadership reporting

These are usually poor fits for Procore anyway.

### Where Procore May Need To Stay

Keep or defer replacement if Level X relies on Procore for:

- Drawing management
- Subcontractor-facing RFIs
- Submittal workflows
- Field daily logs
- Safety documentation
- Change order controls
- Budget/commitment controls
- Owner-required documentation
- Project closeout packages
- Insurance/compliance records

These are high-risk to replace without detailed process mapping.

## Procore Downgrade Plan

### Phase 0: Usage Audit

Goal: understand what Procore actually does for Level X today.

Inputs:

- Procore module list
- User list and seat cost
- Active project count
- Module usage reports
- Export examples
- Current workflows
- Required owner/client reporting
- Accounting/ERP dependencies
- Contractual requirements that mention Procore or equivalent system

Output:

- Keep / replace / downgrade map by module.
- Seat reduction plan.
- Data export and archive requirements.
- Risk register.

Recommended module audit table:

- Module
- Current users
- Actual usage frequency
- Business owner
- External collaborators involved
- Data export requirement
- Contract/compliance dependency
- Replacement complexity
- Replacement priority
- Recommendation: keep, integrate, downgrade, replace, or retire

### Phase 1: Build Around Procore

Goal: create immediate value without disrupting construction ops.

Build:

- Opportunity pipeline
- RFQ tracker
- Qualification engine
- Relationship database
- Executive dashboard
- Procore read-only integration if API access is available

Procore role:

- Remains the construction execution system.
- Level Intelligence OS becomes the front-end pursuit and executive visibility layer.

### Phase 2: Replace Pre-Procore Workflows

Goal: stop using Procore for work it is not good at.

Move into Level Intelligence OS:

- BD pipeline
- Lead sourcing
- Early qualification
- Site intelligence
- Account notes
- Precon opportunity tracking
- Bid/RFQ intake
- Go/no-go decisions
- Leadership reporting

Expected result:

- Fewer users need Procore.
- Procore becomes a narrower construction operations tool.
- Leadership and BD stop relying on Procore dashboards.

### Phase 3: Seat And Module Downgrade

Goal: reduce Procore cost without operational breakage.

Actions:

- Remove executive/BD users from Procore if they only need dashboard visibility.
- Replace Procore reports with Level Intelligence OS dashboards.
- Keep only project ops users in Procore.
- Downgrade modules not tied to field execution or client requirements.
- Archive closed projects outside Procore if contractually safe.

Potential outcome:

- Procore remains for active construction execution.
- Level Intelligence OS handles intelligence, pursuit, RFQ, and executive reporting.
- Seat count drops substantially.

### Phase 4: Selective Module Replacement

Goal: replace operational modules only where ROI is clear.

Possible custom replacements:

- Lightweight RFI tracking
- Lightweight submittal register
- Drawing/document index
- Punch list
- Daily progress notes
- Closeout checklist
- Closeout package tracker
- Owner reporting dashboard

Do not build these until there is evidence that:

- The workflow is simple enough.
- External collaborators will use the system.
- Legal/compliance requirements are understood.
- Data export obligations are covered.
- The replacement saves more than it costs to maintain.

Suggested replacement order:

1. Executive reporting and project visibility.
2. RFQ / bid / go-no-go workflow.
3. Preconstruction tasking and handoff.
4. Document index and closeout package tracking.
5. Lightweight RFI/submittal tracking for simpler projects.
6. Field logs, change controls, and commitments only if Level X has a strong reason to own that software.

### Phase 5: Full Procore Exit Decision

Full exit is only recommended if:

- Most projects do not require Procore-level field collaboration.
- Owner/client contracts do not require Procore or similar tooling.
- Accounting/ERP integration does not depend on Procore.
- Subcontractors can work through a simpler portal.
- Level X accepts the burden of maintaining construction ops software.

If those conditions are not met, the better move is a **Procore downgrade**, not a full replacement.

## Build Roadmap

### MVP: 3-5 Weeks

Goal: one operating view for opportunities and pursuits.

Build:

- Opportunity database
- Account/contact database
- Pipeline stages
- Qualification score
- Executive dashboard
- Manual import
- Document upload
- AI summary for opportunities/RFQs
- Basic role-based access

Success criteria:

- Leadership can see active pursuits and next actions.
- BD/precon can manage opportunities without a spreadsheet.
- At least one weekly executive digest can be generated from live system data.

### Phase 2: Intelligence Layer, 4-8 Weeks

Goal: make the system proactive.

Build:

- Web/news monitoring
- Permit/planning signal ingestion
- Email/document parsing
- AI scoring explanations
- Comparable project matching
- Weekly opportunity digest
- Stale deal alerts

Success criteria:

- New opportunities are surfaced automatically.
- RFQs and planning documents are summarized automatically.
- Opportunity score explains the reasoning clearly enough for human review.

### Phase 3: Enterprise Workflow, 8-12 Weeks

Goal: make it useful across departments.

Build:

- Bid/RFQ workflow
- Go/no-go approval flow
- SSO/SAML
- Audit logs
- Team permissions
- CRM integration
- Procore read-only integration
- Teams/Slack notifications

Success criteria:

- Multiple departments can use the system with appropriate permissions.
- Executives no longer need direct Procore access for visibility.
- Procore downgrade decision can be made from usage evidence.

### Phase 4: Procore Downgrade / Replacement

Goal: reduce Procore dependency.

Build:

- Procore usage dashboard
- Export/archive workflow
- Replacement workflows for pre-Procore activities
- Seat reduction plan
- Optional lightweight construction modules where justified

Success criteria:

- Procore seats/modules reduced where safe.
- No loss of required construction documentation.
- Active project teams retain the tools they need.

## Pitch Narrative

Recommended wording:

> Level X does not need another generic project dashboard. It needs an operating intelligence layer that captures the company's deal flow, relationships, construction judgment, entitlement knowledge, and market signals in one place. We would start upstream of Procore, where opportunities are sourced and qualified, then use the data to decide where Procore is still necessary and where it can be downgraded or replaced.

## Recommendation

Start with **Opportunity Intelligence + Qualification + Executive Dashboard**.

Do not lead with replacing Procore. Lead with:

- Better opportunity visibility.
- Better pursuit discipline.
- Better institutional memory.
- Better executive reporting.
- A path to Procore cost reduction.

The practical strategy is **integrate first, downgrade second, replace selectively third**.

## Open Questions For Level X

- Which Procore modules are currently active?
- How many Procore seats are paid vs actually used?
- Which departments use Procore daily?
- Are owner/client contracts requiring Procore or Procore-like documentation?
- What accounting/ERP system is connected to Procore?
- Where does BD currently track opportunities?
- Where do RFQs and bids currently live?
- Which markets and asset types matter most?
- Who owns go/no-go decisions today?
- What would make leadership say this paid for itself in 90 days?

## Related

- [[Level Intelligence OS - Strategic Dossier]]
- [[Level Intelligence OS - Agentic Architecture Blueprint]]
- [[Level Intelligence OS - ROI and Compounding Value Model]]
- [[Level Intelligence OS - Implementation and Discovery Plan]]
- [[Level Intelligence OS - Internal Strategy Brief]]
