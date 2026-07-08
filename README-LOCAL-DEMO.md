# Level Intelligence OS Demo (Local)

This folder contains the self-contained single-file demo plus a build script that creates live opportunity data.

## 1) Install dependencies

```bash
cd "/Users/omar/Grounded/Projects/Level Intelligence OS"
npm install
```

## 2) Configure environment

```bash
cp .env.example .env
```

Set at least:

- `ANTHROPIC_API_KEY` (required for LLM scoring; optional to use fallback scoring)
- `CHICAGO_APP_TOKEN` (optional; raises API rate limits)

## 3) Generate live demo data

```bash
node scripts/fetch-and-score.mjs
```

Or run both generation and local server in one step:

```bash
npm run demo
```

This writes:

- `data/permits.json` (loaded by the HTML)
- `data/history/YYYY-MM-DD.json` (daily snapshot for history)

## 4) Run the page

Use any static server so the browser can fetch `./data/permits.json`.

```bash
cd "/Users/omar/Grounded/Projects/Level Intelligence OS"
python3 -m http.server 4173
```

Open:

- `http://localhost:4173/level-intelligence-os-demo.html`

### Notes

- If you run `npm run demo`, keep the terminal open while you review the page; stopping the command stops the server.
- The first run writes `data/permits.json` and a snapshot at `data/history/YYYY-MM-DD.json`.

## Web sharing

For sharing a polished, client-ready site (with docs, PDFs, DOCX links, and optional demo), use the GitHub Pages flow described in [`README-SHARING.md`](./README-SHARING.md).

### Runtime behavior

- The HTML is written to prefer `data/permits.json` when available.
- Without a fetchable data file, it falls back to the built-in seeded dataset.
- This keeps the UI unchanged while making the feed truly functional for local runs.
