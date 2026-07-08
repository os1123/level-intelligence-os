---
llm_canonical: true
title: Level Intelligence OS - Implementation and Discovery Plan
aliases:
  - Level Intelligence OS Roadmap
  - Level OS Discovery Plan
type: implementation-plan
status: draft
created: 2026-05-20
updated: 2026-05-20
tags:
  - projects
  - level-x
  - implementation
  - discovery
  - construction
---

# Level Intelligence OS - Implementation and Discovery Plan

## Implementation Philosophy

Build the system in phases that create value early while preserving the long-term architecture.

The first version should not try to replace every system. It should create the central intelligence and decision layer:

- capture signals,
- structure opportunities,
- map relationships,
- score fit,
- route next actions,
- summarize RFQs,
- track approvals,
- and brief leadership.

Once this layer is trusted, Level can expand into deeper preconstruction, permit, financial, project handoff, and software rationalization workflows.

## Phase 0: Discovery And Operating Map

Timeline: 1-2 weeks

### Objective

Understand how Level currently finds, qualifies, pursues, and executes opportunities across construction, development, hospitality, and capital.

### Discovery Workstreams

#### 1. Opportunity Sourcing

Questions:

- Where do new opportunities come from?
- Which sources are most reliable?
- Which sources are noisy?
- Which opportunities are usually discovered too late?
- Who receives inbound RFQs?
- Who monitors permits, planning, zoning, brokers, brands, or development news?
- What does "good opportunity" mean by vertical?

Artifacts to collect:

- current pipeline spreadsheet or CRM export,
- RFQ inbox examples,
- opportunity tracking examples,
- recent wins,
- recent losses,
- recent passes,
- target markets and asset classes.

#### 2. Qualification And Go/No-Go

Questions:

- Who decides whether to pursue?
- What criteria are used?
- Are criteria written down?
- What usually causes a pass?
- What usually causes a regret?
- Which opportunities waste the most time?
- Which patterns predict good economics?

Artifacts to collect:

- go/no-go templates,
- bid review notes,
- executive decision examples,
- project scorecards if any,
- win/loss notes,
- margin history by project type if available.

#### 3. Relationship Management

Questions:

- Where are owner/developer/brand relationships tracked?
- Who owns each major relationship?
- How are follow-ups managed?
- What happens when a relationship owner is unavailable?
- Which accounts are strategically important?
- Which accounts should be touched more often?

Artifacts to collect:

- CRM export,
- contact lists,
- account notes,
- relationship maps,
- email/calendar examples,
- top account list.

#### 4. RFQ And Bid Workflow

Questions:

- Where do RFQs arrive?
- Who reviews them first?
- How are deadlines tracked?
- How are required attachments checked?
- How are prior projects used as comps?
- What causes missed or incomplete submissions?
- How is bid outcome tracked?

Artifacts to collect:

- recent RFQ packages,
- bid checklists,
- submission calendars,
- bid comparison sheets,
- win/loss records,
- standard proposal docs.

#### 5. Permit And Entitlement Workflow

Questions:

- Which jurisdictions matter most?
- Where is permit status tracked?
- How are comments received?
- How are follow-ups handled?
- Which permit types most often delay work?
- Who owns entitlement risk?

Artifacts to collect:

- permit logs,
- sample permit emails,
- portal screenshots or exports,
- jurisdiction contacts,
- plan review comment examples,
- project schedules tied to permits.

#### 6. Existing Software And Data

Questions:

- Which systems are used today?
- Which systems are trusted?
- Which systems are avoided?
- Which systems duplicate each other?
- What is the current software spend?
- Which tools are required by clients or contracts?
- Which systems have API/export access?

Artifacts to collect:

- tool list,
- user/seat list,
- subscription costs,
- CRM export,
- project management export,
- accounting export,
- document folder structure,
- permission model.

### Phase 0 Deliverables

- Current state operating map.
- Data source inventory.
- Opportunity lifecycle map.
- Decision and approval map.
- Initial object model.
- Initial agent map.
- Initial ROI assumptions.
- Implementation backlog.
- 90-day MVP recommendation.

## Phase 1: Foundation And Data Model

Timeline: weeks 1-2 after discovery

### Objective

Create the private operating database and initial interface.

### Build

- Authentication and roles.
- Core database schema.
- Accounts.
- Contacts.
- Relationships.
- Opportunities.
- Sites.
- Markets.
- Jurisdictions.
- Signals.
- RFQs.
- Bids.
- Documents.
- Tasks.
- Decisions.
- Approvals.
- Activity events.
- Scores.
- Audit logs.

### Imports

- accounts and contacts,
- active opportunities,
- current RFQs,
- priority markets,
- historical projects if available,
- vendor/subcontractor list if relevant,
- current permits if relevant.

### Interfaces

- Executive home skeleton.
- Opportunity pipeline.
- Account view.
- Signal inbox.
- Approval queue.
- Admin view.

### Success Criteria

- Core team can log in.
- Active opportunities are visible.
- Accounts and contacts are searchable.
- Each opportunity has owner, stage, next action, and source.
- Leadership can see pipeline state without asking for a spreadsheet.

## Phase 2: Intelligence And Qualification

Timeline: weeks 3-5

### Objective

Make the system intelligent enough to assist with opportunity triage.

### Build

- Signal ingestion workflow.
- AI opportunity summary.
- Dedupe/entity resolution.
- Qualification scoring.
- Relationship brief.
- Similar project lookup.
- Pursue/watch/pass recommendation.
- Next action generation.
- Weekly opportunity digest.

### Agent Capabilities

- Signal Scout Agent.
- Qualification Agent.
- Relationship Agent.
- Executive Briefing Agent, initial version.

### Human Controls

- Human can edit score.
- Human can override recommendation.
- Human must approve external outreach.
- System logs outcome.

### Success Criteria

- New signals can be captured and triaged.
- Opportunity score explains its reasoning.
- Relationship history is visible.
- Weekly digest is generated from live data.
- Leadership can identify top opportunities and stalled pursuits.

## Phase 3: RFQ And Permit Workflows

Timeline: weeks 6-8

### Objective

Move from intelligence to workflow execution support.

### RFQ Build

- RFQ intake.
- RFQ summarization.
- Deadline extraction.
- Required attachment checklist.
- Go/no-go memo.
- Bid task creation.
- Clarification tracking.
- Bid status view.
- Win/loss outcome capture.

### Permit Build

- Permit tracker.
- Permit communication log.
- Status parsing from uploaded/email content where feasible.
- Follow-up reminders.
- Critical path flag.
- Jurisdiction notes.

### Agent Capabilities

- RFQ/Bid Agent.
- Permit/Entitlement Agent.
- Project Handoff Agent, initial version.

### Success Criteria

- RFQs no longer live only in email.
- Deadlines are visible.
- Go/no-go decisions are documented.
- Permit blockers are visible.
- Follow-up responsibilities are clear.

## Phase 4: Executive Operating Rhythm

Timeline: weeks 9-12

### Objective

Make Level Intelligence OS part of weekly management.

### Build

- Weekly executive brief.
- Pending decision queue.
- Stalled opportunity alerts.
- Market activity summary.
- Relationship touch list.
- RFQ deadline summary.
- Permit risk summary.
- Team workload view.
- Outcome tracking.

### Meeting Use

The system should support:

- weekly leadership review,
- BD/precon pipeline meeting,
- RFQ review,
- permit/entitlement risk review,
- monthly strategy review.

### Success Criteria

- Leadership uses the brief as the source of truth.
- Teams update next actions in the system.
- Decisions are captured.
- Outcomes are recorded.
- The system begins showing learning from prior decisions.

## Phase 5: Integrations And Software Rationalization

Timeline: month 4 onward

### Objective

Connect Level Intelligence OS to existing systems and determine what should remain, integrate, downgrade, or be replaced.

### Integration Candidates

- Email.
- Calendar.
- Google Drive or SharePoint.
- CRM.
- Procore or other construction management platform.
- Accounting or ERP.
- Slack or Teams.
- Permit portals where feasible.
- Parcel/ownership data providers.

### Software Rationalization Questions

- Which users only need dashboard visibility?
- Which Procore modules are essential for field execution?
- Which modules are being used as expensive reporting tools?
- Which workflows can move into Level Intelligence OS safely?
- Which tools are contractually required?
- Which data needs archival/export?

### Output

- keep/integrate/downgrade/replace map,
- software spend reduction plan,
- implementation risk register,
- integration roadmap.

## Phase 6: Compounding Intelligence

Timeline: month 6 onward

### Objective

Turn Level's operating history into better recommendations.

### Build

- recommendation accuracy tracking,
- win/loss analysis,
- bid outcome analysis,
- permit cycle time analysis,
- relationship activity analysis,
- vendor performance analysis,
- market signal quality scoring,
- margin prediction inputs,
- playbook generation.

### Questions The System Should Start Answering

- Which signals are worth acting on?
- Which developers are highest value?
- Which project types match Level's best outcomes?
- Which RFQs should Level pass on?
- Which jurisdictions require more planning time?
- Which relationships are going cold?
- Which brands or operators are expanding?
- Which vendors reduce execution risk?

## Roles And Access Model

### Executive

- read executive dashboard,
- review top opportunities,
- approve major decisions,
- review weekly brief,
- see risk and pipeline.

### Business Development

- manage opportunities,
- manage accounts and contacts,
- review signals,
- create next actions,
- draft outreach.

### Preconstruction / Estimating

- manage RFQs,
- review bid requirements,
- compare prior projects,
- track bid tasks,
- prepare go/no-go inputs.

### Development

- manage sites,
- track entitlement,
- manage jurisdictional risk,
- coordinate feasibility.

### Hospitality / Operations

- track acquisition, renovation, brand/operator, opening, and stabilization workflows where applicable.

### Capital / Finance

- review development economics,
- track financing milestones,
- support investor updates,
- review budget and capital decisions.

### Admin

- manage users,
- integrations,
- permissions,
- data imports,
- audit logs.

## Client Meeting Narrative

Recommended sequence:

1. Start with the strategic shift: software can now be owned internally and evolve through language.
2. Explain the analog-to-digital conversion: Level's knowledge is valuable but fragmented.
3. Show the Mercator-like upstream intelligence layer.
4. Show the added operator OS layers.
5. Walk through the opportunity journey.
6. Explain human approval and governance.
7. Explain the compounding data asset.
8. Show phased implementation and early wins.
9. Ask discovery questions.
10. Close on the 90-day pilot.

## 90-Day Pilot Proposal

### Pilot Goal

Prove that Level Intelligence OS can improve opportunity visibility, qualification discipline, RFQ coordination, and executive reporting.

### Pilot Scope

- Active opportunity pipeline.
- Account/contact relationship layer.
- Signal inbox.
- Qualification scoring.
- RFQ intake and go/no-go memo.
- Approval queue.
- Weekly executive brief.

### Pilot Success Metrics

- 100 percent of active pursuits visible.
- Each pursuit has owner, stage, score, and next action.
- Weekly brief generated from system data.
- RFQs tracked with deadlines and status.
- At least 10 signals captured and reviewed.
- Leadership identifies at least 3 decisions faster than current process.
- Clear roadmap for next phase.

## Related

- [[Level Intelligence OS - Strategic Dossier]]
- [[Level Intelligence OS - Agentic Architecture Blueprint]]
- [[Level Intelligence OS - ROI and Compounding Value Model]]
- [[Level Intelligence OS Buildout Plan]]

