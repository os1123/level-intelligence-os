# Deck Materials Package

_Started 2026-05-26 11:31 UTC_

---

## User

can you use the deck guide to make an official deck we can send along with an interactice prototype and a dossier and one pager.

## Assistant

_[tool: read_file]_

_[tool: read_file]_

_[tool: read_file]_

_[tool: list_files]_

_[tool: list_files]_

_[tool: read_file]_

_[tool: read_file]_

_[tool: grep]_

_[tool: update_todos]_

_[tool: copy_starter_component]_

I have a clear picture. The user already has matching one-pager and proposition HTML with an established visual language (executive, paper-and-ink, restrained green/gold accents, sharp corners, dense grids). I'll build the deck in that same visual register so all three artifacts feel like a single kit.

Title sequence (committed to noun-phrase / topic-title style, like book chapters):
1. Level Intelligence OS · 2. Scattered judgment · 3. The cost of scattered judgment · 4. Why now · 5. Category context · 6. The proposition · 7. Outcomes, not code · 8. Signal inbox · 9. Qualification score · 10. Relationship memory · 11. RFQ command center · 12. Approval queue · 13. Executive brief · 14. ROI model · 15. The 90-day pilot · 16. Ownership and close

_[tool: write_file]_

Now I'll build the deck. Single file, static HTML inside `<deck-stage>`, matching the visual language of the existing dossier/one-pager (paper + ink, restrained green/gold/blue accents, sharp corners, executive density).

_[tool: update_todos]_

_[tool: done]_

_[tool: fork_verifier_agent]_

Built the 16-slide deck as `Level Intelligence OS - Deck.html`, matching the visual language of the existing one-pager and proposition (paper + ink, restrained green/gold/blue accents, sharp corners, executive density) so all three artifacts feel like one kit.

**Title sequence** (noun-phrase topic titles, like book chapters):
Title → Scattered judgment → Cost of scattered judgment → Why now → Category context → The proposition → Outcomes, not code → Signal inbox → Qualification score → Relationship memory → RFQ command center → Approval queue → Executive brief → ROI model → 90-day pilot → Ownership and close

**Structural notes**
- Sections grouped (01 problem · 02 why now · 03 proposition · 04 product surfaces · 05 value · 06 engagement · 07 close), with eyebrow + slide counter on every slide for parallelism.
- Two dark-canvas beats — "Outcomes, not code" (7) and "Ownership and close" (16) — give the deck rhythm without using more than 2 background colors total.
- Product surface slides (8–13) share a strict template: left column = title + sources/dimensions, right column = realistic UI mock with chrome, sidebar, table rows, and selected-row highlight.
- Used the Carter Hospitality / Bay Park HGI thread as a continuous example across slides so the system feels lived-in, not abstract.

**Things to consider next**
- Want me to add speaker notes? (They aren't there yet — I'll add them on request.)
- The deck pairs with your existing dossier/one-pager but could also link out from the close slide to the prototype — say the word and I'll wire it.
- If you want to send to client as PPTX/PDF, I can export either format.

## User

Verifier agent check completed

## Assistant

_[tool: str_replace_edit]_

The verifier caught real overflow issues across the product surface slides. Let me fix them systematically — tighten frame padding to gain vertical room, rebalance the inbox grid, fix the slide 10 header overlap, and trim content on the densest slides.

_[tool: grep]_

Got it — repositioning away from Mercator entirely. That's a stronger frame. I'll rewrite slide 5 to be about being purpose-built for Level (not a category comparison), update section labels, and fold in the verifier's overflow fixes for slides 8–13 in the same pass.

_[tool: str_replace_edit]_

## Assistant

_[tool: str_replace_edit]_

Doing this as one batched edit — slide 5 rewrite + section label updates + overflow fixes for slides 8–13.

_[tool: run_script]_

Now the overflow fixes — bulk grid/height changes across slides 8–13 via script, then targeted content trims.

_[tool: grep]_

_[tool: str_replace_edit]_

The script also caught slide 4 — that's fine, the why-now slide also benefits from a wider right column. Now targeted edits: rebalance the inbox grid, fix slide 10 header overlap, and shorten the slide 9 crumb.

_[tool: update_todos]_

_[tool: done]_

_[tool: str_replace_edit]_

Two real overflows left: slide 3 (cost) overshoots by ~70px, slide 1 (title) by 2px. Fixing both.

_[tool: done]_

_[tool: str_replace_edit]_

Two structural fixes needed:

**Slide 1** — my `flex-wrap` made the proof points stack to two lines, pushing content past the bottom. Need to keep them on one line and reduce title size slightly.

**Slide 5** — the 4-quadrant cards have too much content for 2 rows in available space. Need to trim each card.

_[tool: done]_

_[tool: str_replace_edit]_

Slide 12 still has 6 rows that don't fit; slide 11 bid tasks 10px over. Trimming both.

_[tool: done]_

_[tool: str_replace_edit]_

_[tool: done]_

Clean — all overflow validators passing now. Forking the verifier to check the visual composition.

_[tool: fork_verifier_agent]_

Two updates landed:

**Slide 5 reframed — "Built for Level"**
Replaced the Mercator comparison entirely. New slide is a 2×2 of what makes the system Level-specific:
1. **Encodes Level's judgment** — criteria, weights, the exceptions leadership keeps making by hand
2. **Connects Level's relationships** — the relationship graph the company already runs on
3. **Fits how Level works** — RFQ, approval, executive cadence modeled on Level's actual rhythm
4. **Grows with Level** (dark card) — AI providers replaceable, operating memory stays Level's

Section label also retitled "Why now & built for Level." No comparison framing anywhere in the deck now.

**Overflow fixes** — rebalanced the surface slides (wider mocks, taller cards, slimmer sidebar on the inbox, dropped one row on the inbox and two on the approval queue, fixed the slide 10 account header). All clean against validators.

## User

for the examples, i saw you used california examples, can we use illinois and texas instead

also made some updates in the underlying docs: 

More infrastructure additions

and eventually the goal is to help them leave any reliance on monolith software. Now one thing is that they currently use procore as their main working platform. And i think for now we shuld aim to structure out platform around it rather than replace it. Procore is a great source of truth i feel for now. Eventually we can work on replacing that as well. 

lastly, i wonder if its worth mentioning things like market trends and changes happening ot how software is done. with openai's deployment program, the rise of the forward depoloyed expert and engineer etc

## Assistant

_[tool: read_file]_

_[tool: grep]_

Let me check the updated docs to see what's new, then make the changes.

_[tool: read_file]_

_[tool: run_script]_

Lot of changes here. Plan:
1. **Script**: geographic find/replaces (CA → IL/TX) + slide counter renumbering (16 → 18) + section label renumbering
2. **Insert** new slide 5 (Forward-deployed software / market shift)
3. **Insert** new slide 7 (Procore bridge)

_[tool: grep]_

_[tool: grep]_

_[tool: grep]_

_[tool: str_replace_edit]_

Now fix the remaining Long Beach and insert the two new slides.

_[tool: done]_

_[tool: str_replace_edit]_

_[tool: done]_

_[tool: run_script]_

_[tool: done]_

Clean. Forking the verifier on the new 18-slide deck.

_[tool: fork_verifier_agent]_

Updates landed:

**Geographic switch — IL & TX throughout**
- Carter Hospitality Group now Dallas, TX based
- Active opportunity: **Cedar Park HGI** (Cedar Park, TX), Westwell Dallas reposition, West Loop mixed-use (Chicago), Schaumburg & Houston signals
- Comparable work: Hampton Inn Plano, Holiday Inn Express Naperville, Oak Park AC
- Other refs: Frisco AC, Naperville TI, Houston 4th Ward permit

**Two new slides (deck now 18, was 16)**
- **Slide 5 — "Forward-deployed software"** — names the market shift explicitly. 3-column table (Shift / Old pattern / New pattern) covering software fit, work pattern, asset model, delivery. Calls out OpenAI's 2026 deployment program as the visible signal. Closes with "Level can build on the same pattern — privately — and own the compounding memory."
- **Slide 7 — "Procore bridge"** — four phase cards: **Read & reference → Workflow overlay → Evidence-based rationalization → Selective replacement** (dark card for the long-term move). Closes with "The operating principle: earn the right to replace." Procore stays the source of truth for execution while the operating layer wraps it.

**Section restructure**
- Section 02 / Why now (slides 4–5)
- Section 03 / How it fits Level (slides 6–7)
- Section 04 / The proposition (slides 8–9)
- Section 05 / Product (slides 10–15)
- Sections 06–08 follow

Slide counters and labels renumbered throughout. One thing to consider: the deck is now 18 slides; if you want to keep it tighter for a live conversation, the easiest cuts are the product surface slides (any one of 10–15 could go without breaking the flow).

