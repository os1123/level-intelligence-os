# Level Intelligence OS — Sharing & Hosting Guide

## Fast answer
For external sharing, use GitHub Pages.  
Replit-style runtimes are useful for experiments, but Pages is better for:
- a stable brandable link you can send,
- private repository + controlled collaborators,
- predictable versioning (what you send matches a Git commit),
- easy handoff if they want a formal pitch package.

## What this repo now includes
- `scripts/build-share-site.sh`: builds a deployable static folder at `share-site`.
- `publish/index.html`: the main package landing page.
- `publish/files/*`: one-pager / full packet PDFs and DOCX exports.
- `publish/dossier.html`, `publish/proposition.html`, `publish/slides.html`: web pages for review.
- `level-intelligence-os-demo.html`: optional demo page included in the deployed bundle.

## One-click local share preview
```bash
cd "/Users/omar/Grounded/Projects/Level Intelligence OS"
npm ci

# optional (recommended before sharing): refresh demo data snapshot
npm run fetch-data

# build deployable web bundle
npm run share:build

# serve locally
npm run share:serve
```

Then open `http://localhost:4174/` (this serves `share-site`).

## GitHub Pages deployment
1. Commit these files in a GitHub repo.
2. Push to `main`.
3. GitHub Actions will run `deploy-pages.yml` and publish from `share-site`.
4. The public URL appears in:
   - `Actions` → latest `Deploy Level Intelligence OS package` run
   - repository **Settings → Pages**.

The workflow also runs `npm run fetch-data` before building. If external fetches are unavailable, it logs a warning and continues, so deployment still succeeds.

## Required setup (first-time)
- Create a GitHub repo for this folder.
- Set Pages source to `GitHub Actions` (auto-managed by this workflow).
- Ensure branch contains the `.github/workflows/deploy-pages.yml` file.
- Add collaborators for review access as needed.

## Optional: improve demo data freshness
If you want each deployment to run with your Anthropic key:
1. In repo settings, add secret `ANTHROPIC_API_KEY`.
2. (Optional) add `CHICAGO_APP_TOKEN` to reduce Chicago API rate limits.
3. Re-run the workflow (manual via `workflow_dispatch`) or push again.
