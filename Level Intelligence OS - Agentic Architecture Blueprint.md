---
llm_canonical: true
title: Level Intelligence OS - Agentic Architecture Blueprint
aliases:
  - Level Agent Architecture
  - Level Intelligence OS Architecture
type: technical-strategy
status: draft
created: 2026-05-20
updated: 2026-05-20
tags:
  - projects
  - level-x
  - construction
  - agentic-systems
  - architecture
---

# Level Intelligence OS - Agentic Architecture Blueprint

## Architecture Principle

Level Intelligence OS should be built as an internal operating layer, not a loose collection of automations.

The ground-up architecture should have seven layers:

1. Source layer
2. Ingestion layer
3. Domain model layer
4. Knowledge and memory layer
5. Agent layer
6. Workflow and approval layer
7. Interface and reporting layer

Each layer should be independently improvable. This is what makes the system adaptable. If Level changes markets, asset classes, internal roles, or software tools, the operating layer can change without starting over.

## Layer 1: Source Layer

The source layer is everything the system can observe or receive.

### External Sources

- Permit portals
- Planning commission agendas
- City council agendas
- Zoning applications
- Title transfer feeds
- Parcel and ownership datasets
- Commercial real estate listings
- Broker announcements
- Franchise expansion news
- Hospitality development news
- Developer and owner websites
- Public filings
- Local business journals
- Construction bid postings where relevant

### Internal Sources

- Email
- Calendar
- Meeting notes
- CRM records
- Spreadsheets
- RFQ packages
- Bid documents
- Plan files
- Permit correspondence
- Project folders
- Procore or other construction management exports
- Accounting exports
- Relationship notes
- Historical project records
- Executive priorities

### Key Principle

The system should not assume all data starts clean. Most valuable operating data starts messy. The system must accept unstructured language, incomplete records, conflicting names, duplicate contacts, missing dates, and partial context.

## Layer 2: Ingestion Layer

The ingestion layer turns raw sources into usable records.

### Ingestion Jobs

- New signal scan
- Permit email scan
- Planning agenda scan
- RFQ inbox scan
- CRM/contact sync
- File/document indexing
- Calendar event sync
- Manual upload/import
- Historical data migration
- Procore or project-system read-only sync

### Extraction Tasks

Agents or extraction services should identify:

- companies,
- contacts,
- addresses,
- parcels,
- jurisdictions,
- dates,
- deadlines,
- project names,
- asset types,
- estimated values,
- scope descriptions,
- permit numbers,
- plan review comments,
- RFQ requirements,
- decision owners,
- source links,
- and confidence levels.

### Data Quality Controls

Each ingested item should have:

- source,
- timestamp,
- confidence score,
- extraction method,
- human review status,
- duplicate candidate flag,
- and audit trail.

The system should separate "raw observed signal" from "confirmed opportunity." This prevents noisy intelligence from corrupting the operating database.

## Layer 3: Domain Model Layer

The domain model is the map of Level's business.

### Core Objects

- Organization
- User
- Team
- Account
- Contact
- Relationship
- Opportunity
- Signal
- Site
- Parcel
- Market
- Asset type
- Jurisdiction
- Permit
- Planning event
- RFQ
- Bid
- Project
- Vendor/subcontractor
- Investor/capital source
- Document
- Task
- Decision
- Approval
- Activity event
- Score
- Risk
- Integration
- Audit log

### Core Relationships

- Account has contacts.
- Contact has roles and relationship owners.
- Account owns or controls sites.
- Site belongs to market and jurisdiction.
- Opportunity is tied to account, site, asset type, and internal owner.
- Signal may create or update opportunity.
- Opportunity may create RFQ, bid, permit, project, or capital workflow.
- Project has vendors, documents, permits, tasks, decisions, and financial records.
- Decision may require approval.
- Approval has AI recommendation, human decision, outcome, and audit log.
- Score belongs to opportunity, account, RFQ, bid, permit, or vendor.
- Activity event records what happened and why.

### Why This Matters

Generic tools often store records but not the relationships between them. Level needs the relationships because value comes from knowing:

- who owns the site,
- who knows the owner,
- what brand is involved,
- which jurisdiction controls approval,
- which prior Level project is comparable,
- which RFQ history predicts margin risk,
- which internal team should act,
- and which decision is blocking movement.

## Layer 4: Knowledge And Memory Layer

The memory layer makes the system compound.

### Structured Memory

Structured memory includes:

- account history,
- project history,
- bid outcomes,
- score history,
- approval outcomes,
- vendor performance,
- permit cycle times,
- win/loss reasons,
- relationship touches,
- jurisdiction notes,
- and financial outcomes.

### Unstructured Memory

Unstructured memory includes:

- call notes,
- emails,
- RFQ text,
- meeting transcripts,
- permit comments,
- project narratives,
- lessons learned,
- investor updates,
- and internal strategy memos.

### Retrieval

Agents should retrieve both structured and unstructured memory before making recommendations.

Examples:

- "Find similar restaurant buildouts in Houston."
- "What happened last time we worked with this developer?"
- "Which jurisdictions have delayed us most often?"
- "Which RFQs looked attractive but produced poor margins?"
- "Which hotel repositioning deals matched this profile?"

### Feedback

Each recommendation should store:

- what data was used,
- what the agent recommended,
- what the human decided,
- what happened later,
- whether the recommendation was useful,
- and what should change next time.

This is how the system improves.

## Layer 5: Agent Layer

Agents should be specialist operators with tools, permissions, and narrow responsibility. They should not be vague general assistants.

### Orchestrator Agent

Purpose: route user requests, coordinate specialists, and synthesize responses.

Responsibilities:

- understand user intent,
- retrieve relevant context,
- choose specialist agents,
- enforce permissions,
- ask clarifying questions when required,
- produce concise answers,
- and log activity.

### Signal Scout Agent

Purpose: detect and triage potential opportunities.

Responsibilities:

- monitor sources,
- extract entities,
- dedupe signals,
- create signal records,
- propose opportunity records,
- identify asset type and market,
- summarize why the signal matters,
- and route to a human owner.

### Qualification Agent

Purpose: turn Level's judgment into repeatable opportunity scoring.

Responsibilities:

- score opportunity fit,
- explain each score,
- compare to historical opportunities,
- identify missing information,
- recommend pursue/watch/pass,
- suggest next action,
- and learn from outcome.

### Relationship Agent

Purpose: make relationship intelligence actionable.

Responsibilities:

- generate account briefs,
- map contacts,
- identify warm intro paths,
- summarize relationship history,
- flag stale relationships,
- draft outreach,
- recommend next touch,
- and track outcomes.

### RFQ And Bid Agent

Purpose: make RFQ and bid work structured, comparable, and decision-ready.

Responsibilities:

- read RFQ packages,
- extract deadlines and requirements,
- detect missing attachments,
- summarize scope,
- compare to prior bids,
- draft go/no-go memo,
- create bid checklist,
- track clarifications,
- compare vendor bids,
- and summarize award rationale.

### Permit And Entitlement Agent

Purpose: track jurisdictional risk and prevent hidden delays.

Responsibilities:

- monitor permit updates,
- parse plan review comments,
- summarize action required,
- track days in review,
- compare to typical cycle time,
- draft follow-ups,
- flag critical-path blockers,
- and maintain permit communication history.

### Executive Briefing Agent

Purpose: convert system state into leadership operating rhythm.

Responsibilities:

- produce weekly executive brief,
- list top opportunities,
- identify stalled pursuits,
- summarize key changes,
- highlight pending decisions,
- flag risks,
- show team workload,
- and recommend executive focus areas.

### Finance And Capital Agent

Purpose: connect opportunity and project intelligence to economics.

Responsibilities:

- track budgets and high-level financial assumptions,
- summarize financing milestones,
- identify margin risk,
- compare bids to budget,
- support investor reporting,
- track draw or capital events if needed,
- and flag decisions requiring approval.

### Project Handoff Agent

Purpose: move an opportunity into execution cleanly.

Responsibilities:

- create project handoff summary,
- package documents,
- list open decisions,
- summarize relationship and scope context,
- identify risk items,
- create initial tasks,
- and sync relevant data into execution tools.

## Layer 6: Workflow And Approval Layer

The workflow layer turns recommendations into controlled action.

### Authority Levels

| Level | Meaning | Examples |
|---|---|---|
| Autonomous | Agent can act and log | summarize RFQ, classify signal, draft brief, dedupe contact |
| Suggest | Agent creates proposed action | create task, suggest owner, draft email, update stage for review |
| Approval Required | Human must approve before execution | external outreach, bid submission, vendor award, investor note |
| Manual | Human executes with agent support | contract signing, financing, legal, major strategic go/no-go |

### Approval Record

Every approval should include:

- approval type,
- related object,
- requested by,
- requested at,
- amount or business impact if applicable,
- AI recommendation,
- reasoning,
- confidence,
- required approver,
- deadline,
- final decision,
- decision notes,
- executed action,
- outcome,
- and audit trail.

### Example Workflow: New Development Signal

1. Planning agenda is detected.
2. Signal Scout extracts site, owner, hearing date, proposed use.
3. System checks whether account or site already exists.
4. Opportunity candidate is created.
5. Qualification Agent scores fit.
6. Relationship Agent finds contact history.
7. Executive Briefing Agent includes it in weekly digest.
8. Human chooses pursue/watch/pass.
9. System creates next action and owner.
10. Outcome feeds future scoring.

### Example Workflow: RFQ Intake

1. RFQ arrives by email or upload.
2. RFQ Agent extracts scope, deadline, attachments, project location, owner, and required response format.
3. System links RFQ to account, site, and opportunity if possible.
4. Qualification Agent drafts go/no-go memo.
5. Internal owner reviews.
6. If pursue, tasks and bid checklist are created.
7. If external response is drafted, approval is required before sending.
8. Win/loss and margin outcome are stored.

## Layer 7: Interface And Reporting Layer

The interface should be organized around how Level operates.

### Primary Views

- Executive Home
- Signal Inbox
- Opportunity Pipeline
- Account/Relationship View
- Market Map
- RFQ/Bid Command Center
- Permit/Entitlement Tracker
- Approval Queue
- Project Handoff View
- Weekly Brief
- Admin/Permissions

### Executive Home

Should answer:

- What changed this week?
- What should leadership act on?
- Which opportunities matter?
- Which decisions are blocked?
- Which relationships need touch?
- Which RFQs are due?
- Which permits are at risk?
- Which parts of the business are overloaded?
- What did the system learn?

### Search And Natural Language Interface

The system should support questions such as:

- "Show me Houston restaurant opportunities with strong relationship fit."
- "What RFQs are due in the next 10 days?"
- "Which permits are overdue?"
- "Summarize our history with this owner."
- "Which opportunities should we pass on and why?"
- "What changed since last week's executive brief?"
- "Draft a go/no-go memo for this RFQ."
- "What did we learn from lost bids this quarter?"

## Technical Stack Direction

Recommended baseline:

- Next.js web application
- Supabase Postgres for operational database
- Supabase Storage or equivalent for documents
- Row-level security and role-based access
- Background job framework for scheduled scans and syncs
- Model provider abstraction for LLM calls
- Vector search or hybrid retrieval for documents and memory
- Audit logging for all agent actions
- Sentry or equivalent for errors
- Analytics for usage and adoption

The system should avoid hard-coding one model provider as a permanent dependency. The owned asset is Level's data model, workflows, and memory, not any single AI model.

## Non-Negotiable Design Rules

- Humans control consequential decisions.
- Every recommendation must be explainable.
- Every action must be logged.
- Raw signals must be separated from confirmed opportunities.
- Agents must have bounded tools and permissions.
- The data model must support future workflows.
- Import/export must remain available.
- Existing tools should be integrated before they are replaced.
- The system should improve through outcomes, not just prompts.

## Related

- [[Level Intelligence OS - Strategic Dossier]]
- [[Level Intelligence OS - ROI and Compounding Value Model]]
- [[Level Intelligence OS - Implementation and Discovery Plan]]
- [[Level Intelligence OS Buildout Plan]]

