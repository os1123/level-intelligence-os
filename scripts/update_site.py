from pathlib import Path
from shutil import copy2
from textwrap import dedent


ROOT = Path("/Users/omar/Grounded/Projects/Level Intelligence OS")
OFFICIAL = ROOT / "official"
PUBLISH = ROOT / "publish"
PUBLISH_FILES = PUBLISH / "files"

CLIENT_FILES = [
    "Level Intelligence OS - Official One Pager.pdf",
    "Level Intelligence OS - Comprehensive Client Packet.pdf",
    "Level Intelligence OS - Official One Pager.docx",
    "Level Intelligence OS - Comprehensive Client Packet.docx",
    "Level Intelligence OS - Executive Slide Deck.pdf",
]


CSS = r"""
:root{
  --ink:#121820;
  --muted:#5b6775;
  --soft:#eef1ef;
  --line:#d8dde3;
  --paper:#f7f7f4;
  --surface:#ffffff;
  --accent:#0e806c;
  --accent-soft:#e5f3ef;
  --dark:#17202b;
  --yellow:#c99b2e;
  --yellow-soft:#f5ecd8;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{
  margin:0;
  color:var(--ink);
  background:var(--paper);
  font-family:Inter,ui-sans-serif,system-ui,-apple-system,BlinkMacSystemFont,"Segoe UI",sans-serif;
  overflow-x:hidden;
}
a{color:inherit;text-decoration:none}
.nav{
  position:sticky;
  top:0;
  z-index:20;
  min-height:64px;
  padding:0 28px;
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:24px;
  border-bottom:1px solid rgba(18,24,32,.14);
  background:rgba(247,247,244,.9);
  backdrop-filter:blur(16px);
}
.brand{display:flex;align-items:center;gap:12px;min-width:0}
.mark{width:34px;height:34px;border:2px solid var(--ink);display:grid;place-items:center;font-weight:850;letter-spacing:0}
.brand b{display:block;font-size:14px;line-height:1.08}
.brand span{display:block;color:var(--muted);font-size:12px;margin-top:2px}
.links{display:flex;align-items:center;gap:18px;color:var(--muted);font-size:13px;white-space:nowrap}
.links a:hover{color:var(--ink)}
.button{
  display:inline-flex;
  align-items:center;
  justify-content:center;
  min-height:42px;
  padding:0 15px;
  color:#fff;
  background:var(--dark);
  font-size:13px;
  font-weight:800;
  border:1px solid var(--dark);
}
.button.alt{color:var(--ink);background:transparent;border-color:var(--line)}
.hero{
  min-height:calc(100svh - 64px);
  display:grid;
  grid-template-columns:minmax(360px,.9fr) minmax(560px,1.1fr);
  border-bottom:1px solid var(--line);
}
.hero-copy{
  padding:clamp(44px,7vw,92px) 28px;
  display:flex;
  flex-direction:column;
  justify-content:center;
}
.eyebrow{
  margin:0 0 18px;
  color:var(--accent);
  font-size:12px;
  line-height:1;
  font-weight:850;
  letter-spacing:.08em;
  text-transform:uppercase;
}
h1{
  margin:0;
  max-width:11ch;
  font-size:clamp(48px,7vw,104px);
  line-height:.9;
  letter-spacing:0;
  font-weight:650;
}
.lead{
  max-width:58ch;
  margin:26px 0 0;
  color:var(--muted);
  font-size:18px;
  line-height:1.55;
}
.actions{display:flex;flex-wrap:wrap;gap:10px;margin-top:28px}
.hero-points{
  display:grid;
  grid-template-columns:repeat(3,minmax(0,1fr));
  gap:14px;
  max-width:780px;
  margin-top:34px;
}
.hero-points div{border-top:2px solid var(--ink);padding-top:12px}
.hero-points b{display:block;font-size:13px;margin-bottom:7px}
.hero-points span{display:block;color:var(--muted);font-size:13px;line-height:1.35}
.hero-visual{
  border-left:1px solid var(--line);
  padding:clamp(30px,5vw,68px);
  display:grid;
  align-content:center;
  background:var(--soft);
}
.command{
  width:min(100%,820px);
  margin:auto;
  background:var(--surface);
  border:1px solid var(--line);
  box-shadow:0 24px 70px rgba(18,24,32,.1);
}
.command-head{
  display:flex;
  align-items:center;
  justify-content:space-between;
  gap:18px;
  padding:16px 18px;
  border-bottom:1px solid var(--line);
  background:var(--dark);
  color:#fff;
}
.command-head b{font-size:14px}
.command-head span{font-size:12px;color:rgba(255,255,255,.7)}
.command-grid{display:grid;grid-template-columns:1fr 1fr 1fr}
.command-col{min-height:360px;border-right:1px solid var(--line)}
.command-col:last-child{border-right:0}
.command-title{padding:13px 14px;border-bottom:1px solid var(--line);font-size:11px;font-weight:850;letter-spacing:.08em;text-transform:uppercase;color:var(--muted)}
.row{padding:14px;border-bottom:1px solid var(--line)}
.row:last-child{border-bottom:0}
.row b{display:block;font-size:13px;line-height:1.2;margin-bottom:6px}
.row span{display:block;color:var(--muted);font-size:12px;line-height:1.35}
.score{display:flex;align-items:center;gap:8px;margin-top:8px}
.bar{height:7px;flex:1;background:var(--soft)}
.bar i{display:block;height:100%;background:var(--accent)}
.pill{display:inline-flex;align-items:center;min-height:23px;padding:0 8px;border:1px solid var(--line);font-size:11px;color:var(--muted);background:#fff}
section{padding:72px 28px;border-bottom:1px solid var(--line)}
.inner{max-width:1180px;margin:auto}
.split{
  display:grid;
  grid-template-columns:minmax(280px,.72fr) minmax(460px,1fr);
  gap:56px;
  align-items:start;
}
h2{margin:0;font-size:clamp(34px,4.2vw,58px);line-height:1;letter-spacing:0;font-weight:650}
.section-lead{margin:0;color:var(--muted);font-size:17px;line-height:1.56}
.grid-2{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:16px}
.grid-3{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:16px}
.grid-4{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:12px}
.tile{
  border-top:2px solid var(--ink);
  padding-top:14px;
  min-height:120px;
}
.tile b{display:block;font-size:16px;line-height:1.2;margin-bottom:8px}
.tile span,.tile p{display:block;color:var(--muted);font-size:14px;line-height:1.45;margin:0}
.dark{
  margin:0 calc(50% - 50vw);
  padding-left:calc(50vw - 50%);
  padding-right:calc(50vw - 50%);
  background:var(--dark);
  color:#fff;
}
.dark p,.dark span,.dark td{color:rgba(255,255,255,.72)}
.dark .tile{border-color:rgba(255,255,255,.7)}
.dark .button{background:#fff;color:var(--ink);border-color:#fff}
.matrix{width:100%;border-collapse:collapse;background:var(--surface)}
.matrix th,.matrix td{padding:13px 14px;border:1px solid var(--line);vertical-align:top;text-align:left}
.matrix th{background:var(--dark);color:#fff;font-size:12px}
.matrix td{color:var(--muted);font-size:14px;line-height:1.42}
.timeline{display:grid;gap:0;border:1px solid var(--line);background:var(--surface)}
.step{display:grid;grid-template-columns:130px 1fr 1.2fr;border-bottom:1px solid var(--line)}
.step:last-child{border-bottom:0}
.step b,.step span{padding:14px;border-right:1px solid var(--line)}
.step span:last-child{border-right:0}
.step b{font-size:13px}
.step span{color:var(--muted);font-size:14px;line-height:1.4}
.download-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:14px}
.download{
  display:flex;
  min-height:126px;
  flex-direction:column;
  justify-content:space-between;
  padding:16px;
  border:1px solid var(--line);
  background:var(--surface);
  transition:transform .18s ease,border-color .18s ease,background .18s ease;
}
.download:hover{transform:translateY(-2px);border-color:var(--ink);background:#fff}
.download b{font-size:16px}
.download span{color:var(--muted);font-size:13px;line-height:1.35}
.callout{padding:22px;background:var(--accent-soft);border-left:4px solid var(--accent)}
.callout b{display:block;margin-bottom:7px}
.callout p{margin:0;color:var(--muted);line-height:1.5}
.source{font-size:12px;color:var(--muted);line-height:1.45}
.reveal{animation:rise .5s cubic-bezier(.2,.8,.2,1) both}
.reveal:nth-child(2){animation-delay:.06s}.reveal:nth-child(3){animation-delay:.12s}.reveal:nth-child(4){animation-delay:.18s}
@keyframes rise{from{transform:translateY(10px)}to{transform:none}}
@media(max-width:980px){
  .links{display:none}
  .hero{grid-template-columns:1fr;min-height:auto}
  .hero-visual{border-left:0;border-top:1px solid var(--line)}
  .command-grid{grid-template-columns:1fr}
  .command-col{min-height:auto;border-right:0;border-bottom:1px solid var(--line)}
  .command-col:last-child{border-bottom:0}
  .split,.grid-2,.grid-3,.grid-4,.download-grid{grid-template-columns:1fr}
  .hero-points{grid-template-columns:1fr}
  .step{grid-template-columns:1fr}
  .step b,.step span{border-right:0;border-bottom:1px solid var(--line)}
  .step span:last-child{border-bottom:0}
}
@media(max-width:640px){
  .nav{padding:0 18px}
  .hero-copy,.hero-visual,section{padding-left:20px;padding-right:20px}
  h1{font-size:48px}
  .lead{font-size:16px}
  .matrix{display:block;overflow-x:auto;white-space:normal}
  .matrix table{min-width:680px}
}
@media(prefers-reduced-motion:reduce){
  html{scroll-behavior:auto}
  .reveal,.download{animation:none;transition:none}
}
"""


NAV = """
<nav class="nav">
  <a class="brand" href="index.html" aria-label="Level Intelligence OS home">
    <span class="mark">LX</span>
    <span><b>Level Intelligence OS</b><span>Client proposal package</span></span>
  </a>
  <div class="links">
    <a href="#pain">Pain</a>
    <a href="#procore">Procore</a>
    <a href="#system">System</a>
    <a href="#pilot">Pilot</a>
    <a href="#downloads">Downloads</a>
  </div>
</nav>
"""


def page(title, body):
    return dedent(f"""\
    <!doctype html>
    <html lang="en">
    <head>
      <meta charset="utf-8">
      <meta name="viewport" content="width=device-width,initial-scale=1">
      <meta name="description" content="Level Intelligence OS client proposal package.">
      <title>{title}</title>
      <link rel="icon" href="data:,">
      <style>{CSS}</style>
    </head>
    <body>
      {NAV}
      {body}
    </body>
    </html>
    """)


def hero(downloads=True):
    actions = """
      <div class="actions">
        <a class="button" href="Level%20Intelligence%20OS%20-%20Official%20One%20Pager.pdf">Open one-pager PDF</a>
        <a class="button alt" href="Level%20Intelligence%20OS%20-%20Comprehensive%20Client%20Packet.pdf">Open full packet</a>
      </div>
    """ if downloads else ""
    return f"""
    <header class="hero">
      <div class="hero-copy reveal">
        <p class="eyebrow">Official client package</p>
        <h1>Level Intelligence OS</h1>
        <p class="lead">A private construction intelligence operating system built around Level's relationships, RFQs, approvals, Procore reality, and operating judgment.</p>
        {actions}
        <div class="hero-points">
          <div><b>Outcomes, not just code</b><span>Cleaner pursuit visibility, faster RFQ triage, and executive decision rhythm.</span></div>
          <div><b>Procore-first</b><span>Wrap around the source of truth now. Replace modules only where evidence supports it.</span></div>
          <div><b>Compounding memory</b><span>Signals, decisions, wins, losses, and overrides improve the next cycle.</span></div>
        </div>
      </div>
      <div class="hero-visual reveal">
        <div class="command" aria-label="Level Intelligence OS command surface mockup">
          <div class="command-head"><b>Operating Command View</b><span>Find. Qualify. Route. Convert. Learn.</span></div>
          <div class="command-grid">
            <div class="command-col">
              <div class="command-title">Signals</div>
              <div class="row"><b>Planning agenda: hotel conversion</b><span>Market: active. Relationship path: warm. Owner record found.</span><div class="score"><span class="pill">82 fit</span><span class="bar"><i style="width:82%"></i></span></div></div>
              <div class="row"><b>Inbound RFQ package</b><span>Deadline extracted. Insurance requirements flagged. Missing site walk notes.</span><div class="score"><span class="pill">needs review</span><span class="bar"><i style="width:56%"></i></span></div></div>
              <div class="row"><b>Permit activity spike</b><span>Jurisdiction pattern suggests preconstruction movement in target corridor.</span></div>
            </div>
            <div class="command-col">
              <div class="command-title">Decisions</div>
              <div class="row"><b>Pursue / watch / pass</b><span>Recommendation includes relationship strength, margin logic, capacity, and missing information.</span></div>
              <div class="row"><b>Approval queue</b><span>External outreach, bid submission, vendor award, budget, investor, and legal moves require human approval.</span></div>
              <div class="row"><b>Procore bridge</b><span>Project execution remains in Procore while OS adds intelligence and executive workflow above it.</span></div>
            </div>
            <div class="command-col">
              <div class="command-title">Executive Brief</div>
              <div class="row"><b>Changed this week</b><span>3 new signals, 2 RFQs due, 1 stalled approval, 4 relationship follow-ups.</span></div>
              <div class="row"><b>Needs judgment</b><span>One high-score pursuit needs leadership view before outreach.</span></div>
              <div class="row"><b>Learning loop</b><span>Win/loss and override outcomes improve the next recommendation.</span></div>
            </div>
          </div>
        </div>
      </div>
    </header>
    """


def downloads_section():
    return """
    <section id="downloads">
      <div class="inner">
        <div class="split">
          <div>
            <p class="eyebrow">Client-ready files</p>
            <h2>Open the packet in the format that fits the conversation.</h2>
          </div>
          <p class="section-lead">Use the one-pager for the first pass, the comprehensive packet for diligence, and the deck for presentation. The HTML pages are optimized for quick review and static hosting.</p>
        </div>
        <div class="download-grid" style="margin-top:34px">
          <a class="download" href="Level%20Intelligence%20OS%20-%20Official%20One%20Pager.pdf"><b>One-pager PDF</b><span>Executive sheet with pain, value, Procore-first strategy, and pilot terms.</span></a>
          <a class="download" href="Level%20Intelligence%20OS%20-%20Comprehensive%20Client%20Packet.pdf"><b>Comprehensive PDF</b><span>Full proposition with infrastructure, market shift, operating model, ROI, and terms.</span></a>
          <a class="download" href="Level%20Intelligence%20OS%20-%20Official%20One%20Pager.docx"><b>One-pager DOCX</b><span>Editable handout for copy or formatting changes.</span></a>
          <a class="download" href="Level%20Intelligence%20OS%20-%20Comprehensive%20Client%20Packet.docx"><b>Packet DOCX</b><span>Editable comprehensive proposal packet.</span></a>
          <a class="download" href="slides.html"><b>HTML slide deck</b><span>Browser-native presentation path for review or later HyperFrames work.</span></a>
          <a class="download" href="Level%20Intelligence%20OS%20-%20Executive%20Slide%20Deck.pdf"><b>Slide deck PDF</b><span>Exported 19-slide executive presentation.</span></a>
          <a class="download" href="comprehensive-packet.html"><b>Web proposition</b><span>Detailed proposal page optimized for hosting.</span></a>
          <a class="download" href="dossier.html"><b>Dossier page</b><span>Concise client-facing explanation with system areas and pilot path.</span></a>
        </div>
      </div>
    </section>
    """


INDEX_BODY = f"""
<main>
  {hero()}
  <section id="pain">
    <div class="inner">
      <div class="split">
        <div><p class="eyebrow">Pain before platform</p><h2>Level's advantage is real. It is just scattered.</h2></div>
        <p class="section-lead">The highest-value work lives in RFQs, emails, calls, spreadsheets, permit threads, broker notes, project folders, and individual memory. The system makes that judgment searchable, routable, and measurable.</p>
      </div>
      <div class="grid-3" style="margin-top:34px">
        <div class="tile reveal"><b>Scattered signals</b><span>Permits, planning activity, ownership changes, broker notes, franchise news, RFQs, and relationship tips arrive in different places.</span></div>
        <div class="tile reveal"><b>Trapped judgment</b><span>Fit, risk, timing, margin, and relationship context live in individual memory, inboxes, and informal notes.</span></div>
        <div class="tile reveal"><b>Status burden</b><span>Leadership spends time assembling context instead of exercising judgment.</span></div>
      </div>
    </div>
  </section>
  <section class="dark">
    <div class="inner">
      <div class="split">
        <div><p class="eyebrow">Core promise</p><h2>We give you outcomes, not just code.</h2></div>
        <p class="section-lead">Code is the mechanism. The product is operating lift: cleaner pursuit visibility, stronger go/no-go discipline, faster RFQ review, fewer missed follow-ups, and Level-owned operating memory.</p>
      </div>
      <div class="grid-4" style="margin-top:34px">
        <div class="tile"><b>Opportunity capture</b><span>Signals become owned records with source, score, owner, and next action.</span></div>
        <div class="tile"><b>Decision speed</b><span>RFQ facts, blockers, and approvals surface before they become bottlenecks.</span></div>
        <div class="tile"><b>Pursuit discipline</b><span>Level spends less time on poor-fit work and more time on high-fit relationships.</span></div>
        <div class="tile"><b>Compounding memory</b><span>Wins, losses, overrides, and outcomes improve the next recommendation.</span></div>
      </div>
    </div>
  </section>
  <section id="procore">
    <div class="inner">
      <div class="split">
        <div><p class="eyebrow">Procore bridge strategy</p><h2>Procore is the bridge, not the battlefield.</h2></div>
        <p class="section-lead">Level Intelligence OS should wrap around Procore first. Procore remains the execution source of truth while the new layer handles intelligence, RFQs, relationship memory, approvals, and executive decisions.</p>
      </div>
      <div class="timeline" style="margin-top:34px">
        <div class="step"><b>1. Read</b><span>Reference only the Procore data needed for visibility.</span><span>No disruption to field or project teams.</span></div>
        <div class="step"><b>2. Overlay</b><span>Add signal intake, RFQ command center, relationship memory, and executive brief.</span><span>Operating rhythm improves without platform migration.</span></div>
        <div class="step"><b>3. Measure</b><span>Audit which workflows belong in Level-owned software.</span><span>Replacement decisions become evidence-based.</span></div>
        <div class="step"><b>4. Replace</b><span>Move modules only where the owned layer is clearly better.</span><span>Monolith dependence reduces without risky rip-and-replace.</span></div>
      </div>
    </div>
  </section>
  <section>
    <div class="inner">
      <div class="split">
        <div><p class="eyebrow">Category reference</p><h2>We cover the intelligence layers, then add the operating layers.</h2></div>
        <p class="section-lead">Mercator-style tools prove that early construction intelligence matters. Level Intelligence OS should do the useful signal work, but the stronger value is the Level-owned layer those tools do not provide: workflow, approvals, Procore context, operating memory, and continuous improvement.</p>
      </div>
      <table class="matrix" style="margin-top:34px">
        <tr><th>Layer</th><th>Category Tools Usually Cover</th><th>Level-Owned System Adds</th></tr>
        <tr><td>Market and project signals</td><td>Early indicators from permits, planning, projects, and companies.</td><td>Level-specific fit, relationship path, owner assignment, next action, and decision state.</td></tr>
        <tr><td>Company and contact context</td><td>Entity discovery and basic enrichment.</td><td>Internal relationship owners, history, prior bids, trust context, and follow-up rhythm.</td></tr>
        <tr><td>RFQ and document work</td><td>Usually partial or outside the core product.</td><td>Scope extraction, deadline tracking, missing items, risks, go/no-go memo, and bid workflow.</td></tr>
        <tr><td>Execution platform bridge</td><td>Usually not the strategic center.</td><td>Procore remains source of truth while Level OS adds executive intelligence above it.</td></tr>
        <tr><td>Compounding memory</td><td>Vendor data improves the vendor product.</td><td>Level-owned wins, losses, overrides, criteria, and operating judgment improve Level's enterprise asset.</td></tr>
      </table>
    </div>
  </section>
  <section id="system">
    <div class="inner">
      <div class="split">
        <div><p class="eyebrow">Operating system</p><h2>Find, qualify, route, convert, and learn.</h2></div>
        <p class="section-lead">The system turns language-heavy construction work into structured decisions while keeping consequential actions under human control.</p>
      </div>
      <table class="matrix" style="margin-top:34px">
        <tr><th>Module</th><th>What It Does</th><th>Client-Facing Outcome</th></tr>
        <tr><td>Signal inbox</td><td>Captures permits, planning agendas, ownership changes, broker notes, RFQs, CRM, and email activity.</td><td>Early signals become reviewable records.</td></tr>
        <tr><td>Qualification engine</td><td>Scores pursue, watch, or pass using Level-specific criteria and reasoning.</td><td>Leadership spends less time on poor-fit work.</td></tr>
        <tr><td>RFQ command center</td><td>Extracts scope, deadlines, addenda, missing items, risks, and go/no-go memo.</td><td>RFQs become decision-ready work.</td></tr>
        <tr><td>Approval queue</td><td>Routes recommendations, evidence, confidence, approver, and decision state.</td><td>Agents prepare work while humans control consequential actions.</td></tr>
        <tr><td>Executive brief</td><td>Summarizes changes, stuck items, RFQs due, approvals, and relationship follow-ups.</td><td>Leadership gets a weekly decision rhythm from live system data.</td></tr>
      </table>
    </div>
  </section>
  <section id="pilot">
    <div class="inner">
      <div class="split">
        <div><p class="eyebrow">90-day pilot</p><h2>A contained build with visible operating value.</h2></div>
        <p class="section-lead">The pilot proves usefulness in workflows Level already runs: opportunity review, RFQ triage, relationship follow-up, approval routing, and executive reporting.</p>
      </div>
      <div class="timeline" style="margin-top:34px">
        <div class="step"><b>Weeks 1-2</b><span>Foundation</span><span>Data model, active pursuits, account/contact layer, executive dashboard skeleton.</span></div>
        <div class="step"><b>Weeks 3-5</b><span>Intelligence</span><span>Signal inbox, opportunity summaries, scoring, relationship briefs.</span></div>
        <div class="step"><b>Weeks 6-8</b><span>Workflow</span><span>RFQ command center, deadline extraction, go/no-go memo, approval queue.</span></div>
        <div class="step"><b>Weeks 9-12</b><span>Rhythm</span><span>Weekly executive brief, outcome tracking, adoption review, phase-two roadmap.</span></div>
      </div>
    </div>
  </section>
  {downloads_section()}
</main>
"""


COMPREHENSIVE_BODY = f"""
<main>
  {hero()}
  <section id="pain">
    <div class="inner">
      <div class="split">
        <div><p class="eyebrow">Executive thesis</p><h2>Build the operating memory that makes Level sharper.</h2></div>
        <p class="section-lead">Level already has trusted relationships, construction judgment, development instincts, hospitality experience, capital discipline, vendor memory, and practical pattern recognition. The opportunity is to turn that judgment into a private operating system Level owns.</p>
      </div>
      <div class="grid-2" style="margin-top:34px">
        <div class="callout"><b>Near-term outcome</b><p>Cleaner active pipeline, faster RFQ review, better go/no-go discipline, and weekly executive visibility.</p></div>
        <div class="callout"><b>Long-term asset</b><p>A Level-owned operating memory that improves pursuit, relationship leverage, execution handoff, and software adaptability.</p></div>
      </div>
    </div>
  </section>
  <section>
    <div class="inner">
      <div class="split">
        <div><p class="eyebrow">Built for Level</p><h2>Not a vendor clone. Not a rip-and-replace pitch.</h2></div>
        <p class="section-lead">Mercator and similar tools are useful category references because they show that earlier construction intelligence has value. The strategic point is different: Level should own software built around Level's relationships, standards, RFQ process, approval rules, markets, capital context, and executive rhythm.</p>
      </div>
      <table class="matrix" style="margin-top:34px">
        <tr><th>Generic Vendor Logic</th><th>Level Intelligence OS Logic</th></tr>
        <tr><td>Expose market or project signals.</td><td>Translate signals into Level-specific opportunities, owners, scores, and next actions.</td></tr>
        <tr><td>Use vendor-defined fields and workflows.</td><td>Represent Level's domain model: accounts, contacts, sites, RFQs, permits, bids, approvals, relationships, and decisions.</td></tr>
        <tr><td>Optimize for broad adoption.</td><td>Optimize for Level's operating judgment, pursuit discipline, leadership rhythm, and long-term ownership.</td></tr>
      </table>
      <table class="matrix" style="margin-top:24px">
        <tr><th>Layer</th><th>What Category Intelligence Tools Usually Do</th><th>What We Add For Level</th></tr>
        <tr><td>Signal discovery</td><td>Find early construction, company, permit, and planning signals.</td><td>Turn each signal into a Level-owned opportunity with fit score, owner, confidence, next action, and audit trail.</td></tr>
        <tr><td>Market awareness</td><td>Show which projects and companies are active.</td><td>Connect activity to Level's markets, hospitality/development thesis, relationship access, and capacity.</td></tr>
        <tr><td>Relationship context</td><td>May surface external companies or people.</td><td>Preserve internal relationship owners, prior touches, trust history, next follow-up, and executive context.</td></tr>
        <tr><td>RFQ operations</td><td>Usually not the central workflow.</td><td>Extract requirements, risks, deadlines, missing items, comparable work, and go/no-go memo.</td></tr>
        <tr><td>Approvals and governance</td><td>Usually outside the product or generic.</td><td>Define Level-specific authority gates, review queues, audit logs, and human approval rules.</td></tr>
        <tr><td>Procore bridge</td><td>Not designed to become Level's internal software layer.</td><td>Use Procore as source of truth now while building the owned intelligence layer above it.</td></tr>
        <tr><td>Compounding enterprise value</td><td>Learning stays inside the vendor product.</td><td>Level's wins, losses, overrides, definitions, and operating judgment become a proprietary asset.</td></tr>
      </table>
    </div>
  </section>
  <section>
    <div class="inner">
      <div class="split">
        <div><p class="eyebrow">Proven infrastructure</p><h2>Known construction-platform primitives, Level-specific product.</h2></div>
        <p class="section-lead">The build can reuse internal construction-platform patterns: connected domain models, workflow state machines, specialist agents, human controls, document intelligence, operating dashboards, and feedback loops.</p>
      </div>
      <div class="grid-3" style="margin-top:34px">
        <div class="tile"><b>Domain model</b><span>Accounts, contacts, sites, projects, permits, RFQs, bids, approvals, outcomes, and notes.</span></div>
        <div class="tile"><b>Workflow state</b><span>Opportunities, RFQs, permits, approvals, and vendor workflows move through explicit statuses.</span></div>
        <div class="tile"><b>Human control</b><span>Authority levels, approvals, audit logs, escalation rules, and explicit review.</span></div>
      </div>
    </div>
  </section>
  <section id="procore">
    <div class="inner">
      <div class="split">
        <div><p class="eyebrow">Procore bridge</p><h2>Earn the right to replace.</h2></div>
        <p class="section-lead">The first move is not to replace Procore. The first move is to wrap around it, create measurable value, and let usage evidence determine what eventually moves into Level-owned software.</p>
      </div>
      <div class="timeline" style="margin-top:34px">
        <div class="step"><b>Read</b><span>Procore remains the current project source of truth.</span><span>Reference only what improves visibility and decisions.</span></div>
        <div class="step"><b>Overlay</b><span>Level OS handles signals, RFQs, approvals, relationship memory, and briefs.</span><span>No operational disruption.</span></div>
        <div class="step"><b>Rationalize</b><span>Measure friction, usage, seats, modules, and reporting gaps.</span><span>Build a Procore downgrade/replacement roadmap with evidence.</span></div>
      </div>
    </div>
  </section>
  <section>
    <div class="inner">
      <div class="split">
        <div><p class="eyebrow">Market shift</p><h2>Software is becoming forward-deployed and company-specific.</h2></div>
        <div>
          <p class="section-lead">The market is moving from fixed SaaS screens toward AI systems deployed inside real workflows. OpenAI's Deployment Company and forward-deployed engineering model are a clear signal that enterprise value increasingly comes from workflow fit, deployment expertise, governance, and measurable outcomes.</p>
          <p class="source" style="margin-top:14px">Reference: <a href="https://openai.com/index/openai-launches-the-deployment-company/">OpenAI Deployment Company announcement</a> and <a href="https://openai.com/business/the-openai-deployment-company">forward deployed engineering at OpenAI</a>.</p>
        </div>
      </div>
    </div>
  </section>
  <section id="system">
    <div class="inner">
      <div class="split">
        <div><p class="eyebrow">Agentic structure</p><h2>Specialist workflows under one governance model.</h2></div>
        <p class="section-lead">The system should not be one vague assistant. It should be a set of bounded workflows with clear inputs, tools, authority levels, and escalation paths.</p>
      </div>
      <table class="matrix" style="margin-top:34px">
        <tr><th>Workflow Agent</th><th>Role</th><th>Human Control</th></tr>
        <tr><td>Signal Scout</td><td>Finds, dedupes, summarizes, and routes project signals.</td><td>Autonomous, logged.</td></tr>
        <tr><td>Qualification</td><td>Scores opportunities against Level-specific criteria.</td><td>Suggests pursue, watch, or pass.</td></tr>
        <tr><td>RFQ/Bid</td><td>Extracts requirements, deadlines, risks, and go/no-go memos.</td><td>Bid submissions require approval.</td></tr>
        <tr><td>Executive Briefing</td><td>Turns system activity into a weekly decision brief.</td><td>Leadership decides final actions.</td></tr>
      </table>
    </div>
  </section>
  <section class="dark">
    <div class="inner">
      <div class="split">
        <div><p class="eyebrow">ROI model</p><h2>Operational first, strategic second, compounding third.</h2></div>
        <p class="section-lead">The value is not only labor savings. The larger value is better pursuit discipline, faster decisions, fewer blind spots, stronger relationship leverage, and proprietary operating memory.</p>
      </div>
      <div class="grid-4" style="margin-top:34px">
        <div class="tile"><b>Capture</b><span>Signals captured, time to first action, conversion by source.</span></div>
        <div class="tile"><b>Discipline</b><span>Go/no-go cycle time, win rate by score, avoided pursuit hours.</span></div>
        <div class="tile"><b>Risk</b><span>Missed deadline rate, response time, unresolved blocker age.</span></div>
        <div class="tile"><b>Memory</b><span>Record completeness, reuse of history, recommendation accuracy.</span></div>
      </div>
    </div>
  </section>
  <section id="pilot">
    <div class="inner">
      <div class="split">
        <div><p class="eyebrow">Pilot path</p><h2>Prove value in 90 days.</h2></div>
        <p class="section-lead">Success means active pursuits visible, RFQs tracked, signals reviewed and routed, weekly executive briefs generated from live system data, and a phase-two roadmap based on observed value.</p>
      </div>
      <div class="timeline" style="margin-top:34px">
        <div class="step"><b>1-2</b><span>Foundation</span><span>Data model, roles, active opportunities, account/contact layer.</span></div>
        <div class="step"><b>3-5</b><span>Intelligence</span><span>Signal inbox, summaries, scoring, relationship briefs.</span></div>
        <div class="step"><b>6-8</b><span>Workflow</span><span>RFQ command center, deadlines, go/no-go memo, approval queue.</span></div>
        <div class="step"><b>9-12</b><span>Rhythm</span><span>Weekly brief, outcome tracking, adoption review, roadmap.</span></div>
      </div>
    </div>
  </section>
  {downloads_section()}
</main>
"""


DOSSIER_BODY = f"""
<main>
  {hero()}
  <section id="pain">
    <div class="inner">
      <div class="split">
        <div><p class="eyebrow">Dossier summary</p><h2>The message to Level.</h2></div>
        <p class="section-lead">Level Intelligence OS is a private operating layer around how Level finds, qualifies, routes, and converts opportunities. It starts by wrapping around Procore, not replacing it, then compounds value through Level-owned operating memory.</p>
      </div>
      <div class="grid-3" style="margin-top:34px">
        <div class="tile"><b>Pain</b><span>Judgment is scattered across RFQs, emails, calls, spreadsheets, permit threads, broker notes, and memory.</span></div>
        <div class="tile"><b>Promise</b><span>Outcomes, not just code: faster triage, cleaner visibility, and fewer missed follow-ups.</span></div>
        <div class="tile"><b>Asset</b><span>Level owns the data, domain model, workflow definitions, and generated operating memory.</span></div>
      </div>
    </div>
  </section>
  <section id="procore">
    <div class="inner">
      <div class="split">
        <div><p class="eyebrow">Implementation stance</p><h2>Build around the current source of truth.</h2></div>
        <p class="section-lead">Procore remains the execution system first. Level Intelligence OS adds the upstream and executive layer: signals, qualification, RFQs, relationship memory, approval routing, and weekly briefs.</p>
      </div>
    </div>
  </section>
  <section id="system">
    <div class="inner">
      <table class="matrix">
        <tr><th>System Area</th><th>Client-Facing Outcome</th></tr>
        <tr><td>Signal inbox</td><td>Early project, permit, planning, ownership, franchise, broker, and RFQ signals captured in one place.</td></tr>
        <tr><td>Qualification engine</td><td>Pursue, watch, or pass recommendations based on Level-specific fit criteria.</td></tr>
        <tr><td>RFQ command center</td><td>Scope summaries, deadlines, missing requirements, go/no-go memos, and bid tasks.</td></tr>
        <tr><td>Executive brief</td><td>Weekly view of what changed, what is stuck, and what leadership must decide.</td></tr>
      </table>
    </div>
  </section>
  {downloads_section()}
</main>
"""


PACKAGE_BODY = INDEX_BODY


def write(path, html):
    path.write_text(html, encoding="utf-8")


def main():
    OFFICIAL.mkdir(exist_ok=True)
    PUBLISH.mkdir(exist_ok=True)
    PUBLISH_FILES.mkdir(exist_ok=True)

    official_pages = {
        "package.html": page("Level Intelligence OS - Official Package", PACKAGE_BODY),
        "index.html": page("Level Intelligence OS - One Page", INDEX_BODY),
        "dossier.html": page("Level Intelligence OS - Dossier", DOSSIER_BODY),
        "comprehensive-packet.html": page("Level Intelligence OS - Comprehensive Client Packet", COMPREHENSIVE_BODY),
    }
    publish_pages = {
        "index.html": page("Level Intelligence OS", INDEX_BODY.replace('href="Level%20Intelligence%20OS%20-%20', 'href="files/Level%20Intelligence%20OS%20-%20').replace('href="comprehensive-packet.html"', 'href="proposition.html"').replace('href="dossier.html"', 'href="dossier.html"')),
        "proposition.html": page("Level Intelligence OS - Detailed Proposition", COMPREHENSIVE_BODY.replace('href="Level%20Intelligence%20OS%20-%20', 'href="files/Level%20Intelligence%20OS%20-%20').replace('href="comprehensive-packet.html"', 'href="proposition.html"').replace('href="dossier.html"', 'href="dossier.html"')),
        "dossier.html": page("Level Intelligence OS - Dossier", DOSSIER_BODY.replace('href="Level%20Intelligence%20OS%20-%20', 'href="files/Level%20Intelligence%20OS%20-%20').replace('href="comprehensive-packet.html"', 'href="proposition.html"').replace('href="dossier.html"', 'href="dossier.html"')),
        "visual.html": page("Level Intelligence OS - Visual", INDEX_BODY.replace('href="Level%20Intelligence%20OS%20-%20', 'href="files/Level%20Intelligence%20OS%20-%20').replace('href="comprehensive-packet.html"', 'href="proposition.html"').replace('href="dossier.html"', 'href="dossier.html"')),
    }

    for filename, html in official_pages.items():
        write(OFFICIAL / filename, html)
    for filename, html in publish_pages.items():
        write(PUBLISH / filename, html)
    for filename in CLIENT_FILES:
        source = OFFICIAL / filename
        if source.exists():
            copy2(source, PUBLISH_FILES / filename)
    if (OFFICIAL / "slides.html").exists():
        copy2(OFFICIAL / "slides.html", PUBLISH / "slides.html")
    print("Updated official and publish HTML site files.")


if __name__ == "__main__":
    main()
