#!/usr/bin/env node

import fs from "node:fs/promises";
import path from "node:path";
import { fileURLToPath } from "node:url";

import Anthropic from "@anthropic-ai/sdk";
import dotenv from "dotenv";

dotenv.config();

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT_DIR = path.resolve(__dirname, "..");
const DATA_DIR = path.join(ROOT_DIR, "data");

const CONFIG = {
  endpoint: "https://data.cityofchicago.org/resource/ydr8-5enu.json",
  issueAfter: process.env.CHICAGO_ISSUE_AFTER || "2026-01-01T00:00:00",
  limit: Number(process.env.CHICAGO_LIMIT || "600"),
  targetCount: Number(process.env.TARGET_OPPS || "15"),
  appToken: process.env.CHICAGO_APP_TOKEN || "",
  cityAreaKeywords: [
    "restaurant",
    "kitchen",
    "hood",
    "cafe",
    "bar",
    "tenant",
    "build-out",
    "buildout",
    "retail",
    "food",
    "dining",
    "take out",
    "counter",
    "kitchen renovation",
    "tenant improvement"
  ],
  permittedTypes: [
    "PERMIT - NEW CONSTRUCTION",
    "PERMIT - RENOVATION/ALTERATION",
    "PERMIT - RENOVATION / ALTERATION",
    "PERMIT – RENOVATION/ALTERATION",
    "PERMIT – NEW CONSTRUCTION",
    "PERMIT – EXPRESS PERMIT PROGRAM",
    "PERMIT - EXPRESS PERMIT PROGRAM"
  ],
  minReportedCost: Number(process.env.CHICAGO_MIN_REPORTED_COST || "100000"),
  targetAreas: ["West Loop", "Fulton Market", "River North"],
  modelCandidates: [
    process.env.ANTHROPIC_MODEL || "claude-opus-4-8",
    "claude-3-5-sonnet-20241022",
    "claude-3-5-sonnet-latest"
  ]
};

const RUN_AT = new Date().toISOString();
const hasAnthropic = Boolean(process.env.ANTHROPIC_API_KEY);

function normalizeText(value) {
  if (value == null) return "";
  return String(value).trim();
}

function parseMoney(value) {
  const n = Number(String(value || "").replace(/[^0-9.-]/g, ""));
  return Number.isFinite(n) ? Math.max(0, n) : 0;
}

function parseDate(value) {
  if (!value) return null;
  const d = new Date(value);
  return Number.isNaN(d.valueOf()) ? null : d;
}

function makeFiledLabel(date) {
  if (!date) return "TBD";
  return date.toLocaleDateString("en-US", { month: "short", day: "numeric" });
}

function makeAddress(record) {
  return [
    normalizeText(record.street_number),
    normalizeText(record.street_direction || record.street_direction_name),
    normalizeText(record.street_name)
  ].filter(Boolean).join(" ").trim() || "Chicago property";
}

function makeHood(record) {
  return normalizeText(record.community_area_name || record.community_area || record.nbrhood || "Chicago") || "Chicago";
}

function inferType(record) {
  const candidate = normalizeText(record.permit_type || record.permit_subtype || record.permit_sub_type || record.work_description).toLowerCase();
  if (/(fast.?casual|restaurant|full.?service|bistro|cafe|dining|kitchen|bar|food)/.test(candidate)) {
    if (candidate.includes("cafe")) return "Restaurant/Café Build-out";
    if (candidate.includes("retail") && candidate.includes("restaurant")) return "Restaurant + Retail Build-out";
    if (candidate.includes("fast") && candidate.includes("casual")) return "Fast-Casual Build-out";
    return "Restaurant Build-out";
  }
  if (candidate.includes("retail")) return "Retail Conversion / Build-out";
  return normalizeText(record.permit_type || "Permit" );
}

function inferSqft(record) {
  const candidates = [record.sq_ft, record.revised_sq_ft, record.total_sq_ft, record.bldg_area, record.site_area, record.area_sq_ft];
  for (const c of candidates) {
    const n = parseMoney(c);
    if (n > 0) {
      return `${n.toLocaleString("en-US")} sf`;
    }
  }
  return "—";
}

function inferOwner(record) {
  const candidates = [
    record.applicant,
    record.permit_holder,
    record.contact_name,
    record.property_owner,
    record.owner,
    "Unknown owner"
  ];
  return candidates.map(normalizeText).find(Boolean);
}

function inferContractor(record) {
  const candidates = [
    record.contractor,
    record.general_contractor,
    record.contractor_name,
    record.construction_manager,
    "Not yet selected"
  ];
  return candidates.map(normalizeText).find(Boolean) || "Not yet selected";
}

function inferArchitect(record) {
  const candidates = [record.architect,
    record.design_professional,
    record.architectural_firm,
    record.architect_name,
    "—"
  ];
  return candidates.map(normalizeText).find(Boolean) || "—";
}

function inferBrand(record) {
  const candidates = [
    record.trading_name,
    record.applicant,
    record.business_name,
    record.organization_name,
    "Prospective operator"
  ];
  return candidates.map(normalizeText).find(Boolean) || "Prospective operator";
}

function isRestaurantRetail(record) {
  const haystack = [record.work_description, record.permit_type, record.permit_subtype, record.permit_sub_type, record.description]
    .filter(Boolean)
    .join(" ")
    .toLowerCase();

  const permitType = normalizeText(record.permit_type)
    .toUpperCase()
    .replace(/[–—]/g, "-");

  const hasPermitType = CONFIG.permittedTypes.some((type) => permitType === type)
    || /PERMIT\s*-\s*(NEW CONSTRUCTION|RENOVATION\/?ALTERATION?|EXPRESS PERMIT PROGRAM|PERMIT)/.test(permitType)
    || !permitType;
  const hasKeyword = CONFIG.cityAreaKeywords.some(keyword => haystack.includes(keyword));
  return (hasPermitType || /PERMIT/.test(permitType)) && hasKeyword;
}

function normalizeRecord(record) {
  const issueDate = parseDate(record.issue_date) || parseDate(record.application_start_date) || parseDate(record.creation_date);
  const owner = inferOwner(record);
  const brand = inferBrand(record);
  const cost = parseMoney(record.reported_cost);

  return {
    id: normalizeText(record.permit_ || record.id || `${record.permit_no || "P"}-${issueDate ? issueDate.getTime() : Date.now()}`),
    addr: makeAddress(record),
    hood: makeHood(record),
    type: inferType(record),
    cost,
    sqft: inferSqft(record),
    filed: issueDate ? makeFiledLabel(issueDate) : "TBD",
    filedDate: issueDate ? issueDate.toISOString() : null,
    status: normalizeText(record.permit_status || record.status || "Under review"),
    desc: normalizeText(record.work_description || record.description || record.short_description || `Permit for ${inferType(record).toLowerCase()} activity`).slice(0, 220),
    owner,
    brand,
    contractor: inferContractor(record),
    arch: inferArchitect(record),
    raw: {
      permitType: normalizeText(record.permit_type),
      application: normalizeText(record.permit_ || record.id),
      applicantAddress: makeAddress(record),
      reportedCost: cost,
      permitStatus: normalizeText(record.status),
      rawDate: issueDate ? issueDate.toISOString() : null,
      communityArea: normalizeText(record.community_area || record.community_area_name),
      ward: normalizeText(record.ward),
      contractorRaw: normalizeText(record.contractor || record.general_contractor),
      applicantRaw: normalizeText(record.applicant || record.permit_holder)
    }
  };
}

function heuristicScore(record) {
  let score = 55;
  const reasons = [];

  const inArea = CONFIG.targetAreas.includes(record.hood);
  if (inArea) {
    score += 18;
    reasons.push({ d: "up", t: `<b>${record.hood}</b> is a high-density area for Level's Chicago historical activity.` });
  }

  if (record.cost >= 800000 && record.cost <= 2000000) {
    score += 20;
    reasons.push({ d: "up", t: `<b>$${(record.cost / 1_000_000).toFixed(2)}M</b> sits near Level's preferred deal band.` });
  } else if (record.cost > 2000000) {
    score -= 8;
    reasons.push({ d: "dn", t: "Reported cost is above Level's preferred scope band for this focused wedge." });
  } else if (record.cost < 250000) {
    score -= 12;
    reasons.push({ d: "dn", t: "Low reported cost creates limited upside relative to mobilization burden." });
  }

  if ((record.contractor || "").toLowerCase().includes("not yet selected") || !record.contractor) {
    score += 10;
    reasons.push({ d: "up", t: "No GC named yet; pursuit window is still open." });
  }

  const desc = normalizeText(record.desc || "").toLowerCase();
  if (/(food|restaurant|kitchen|dining|bar|cafe)/.test(desc)) {
    score += 8;
  }

  const finalScore = Math.max(35, Math.min(99, Math.round(score)));
  let rec = "watch";
  if (finalScore >= 82) rec = "pursue";
  else if (finalScore <= 52) rec = "pass";

  while (reasons.length < 3) {
    reasons.push({ d: "nu", t: "Signal quality and fit are pending on owner-level confirmation from linked records." });
  }

  return { score: finalScore, rec, reasons: reasons.slice(0, 4) };
}

function extractText(resp) {
  if (!resp || !Array.isArray(resp.content) || resp.content.length === 0) return "";
  return resp.content
    .filter((c) => c && c.type === "text" && typeof c.text === "string")
    .map((c) => c.text)
    .join("\n");
}

function parseScoringResponse(text) {
  if (!text) throw new Error("No model text response");
  const match = text.match(/\{[\s\S]*\}/);
  if (!match) throw new Error("Model output did not include JSON");

  const parsed = JSON.parse(match[0]);
  const rec = String(parsed.rec || "").toLowerCase();
  const score = Number(parsed.score);

  if (!Number.isFinite(score) || score < 0 || score > 100) {
    throw new Error("Invalid score from model");
  }
  if (!new Set(["pursue", "watch", "pass"]).has(rec)) {
    throw new Error("Invalid recommendation from model");
  }

  const reasons = Array.isArray(parsed.reasons)
    ? parsed.reasons
        .map((r) => ({
          d: new Set(["up", "dn", "nu"]).has(r.d) ? r.d : "nu",
          t: normalizeText(r.t).replace(/\"/g, "") || "Scored on fit, geography, and project maturity."
        }))
        .slice(0, 4)
    : [];

  while (reasons.length < 3) {
    reasons.push({ d: "nu", t: "Scoring model provided additional context not required for this pass." });
  }

  return { score: Math.round(score), rec, reasons: reasons.slice(0, 4) };
}

async function scoreRecord(record, anthropic) {
  if (!hasAnthropic || !anthropic) {
    return heuristicScore(record);
  }

  const system = "You are a restaurant & retail construction opportunity intelligence analyst for a Chicago contractor. "
    + "Score only opportunities where this firm already owns comparable restaurant/retail execution workflows. "
    + "Return strict JSON only, no Markdown, in this exact shape: { \"score\":0-100 integer, \"rec\":\"pursue|watch|pass\", \"reasons\":[{\"d\":\"up|dn|nu\",\"t\":\"text\"}] }. "
    + "Use 3-5 reasons. Keep reasons specific to this permit text and fields.";

  const prompt = {
    id: record.id,
    addr: record.addr,
    hood: record.hood,
    type: record.type,
    cost: record.cost,
    status: record.status,
    desc: record.desc,
    owner: record.owner,
    contractor: record.contractor,
    recency: record.filed
  };

  const rubric = `Scoring rubric:\n`+
    `- Asset-class fit: full-service/fast-casual / restaurant retail buildouts score up; office amenity/non-restaurant score down.\n`+
    `- Deal size: strongest when reported cost is $800K - $2M. Below ~$250K should be down-weighted.\n`+
    `- Geography: West Loop / Fulton Market / River North are up-weighted.\n`+
    `- No GC named: open pursuit window, up-weight.\n`+
    `- Known repeat developer / franchise developer signals are up-weighted.\n`;

  let lastErr;
  for (const model of CONFIG.modelCandidates) {
    try {
      const result = await anthropic.messages.create({
        model,
        max_tokens: 800,
        temperature: 0.2,
        system: `${system}\n\n${rubric}`,
        messages: [{ role: "user", content: JSON.stringify(prompt) }]
      });
      const text = extractText(result);
      return { model, ...(parseScoringResponse(text)) };
    } catch (err) {
      lastErr = err;
    }
  }

  if (lastErr) {
    console.warn(`Model scoring failed for ${record.id}; using heuristic fallback.`, lastErr.message);
  }

  return { model: "heuristic", ...heuristicScore(record) };
}

function buildActions(record) {
  return [
    { ic: "✦", t: "Generate owner brief", d: `Resolve ${record.owner} principal and recent history before outreach.`, gate: false, primary: true },
    { ic: "✎", t: "Draft go/no-go memo", d: "Summarize scope, margins, and timing risks from permit signal and internal rubric.", gate: false },
    { ic: "✉", t: "Draft intro to owner", d: "Draft outreach if pursuit criteria are met and approval is granted.", gate: true }
  ];
}

function buildTimeline(record, scoreResult) {
  const at = parseDate(record.raw.rawDate) || new Date();
  const t = at.toLocaleString("en-US", { month: "short", day: "numeric", hour: "2-digit", minute: "2-digit" });
  return [
    { when: `${t}`, who: "Opportunity Scout", what: `Detected permit ${record.id} in Chicago permit feed.`, agent: true },
    {
      when: `${t}`,
      who: "Qualification Agent",
      what: `Scored ${scoreResult.score} / ${scoreResult.rec.toUpperCase()} using configured rubric + model output.`,
      agent: true
    }
  ];
}

async function fetchAndNormalizeRecords(issueAfter, useKeywordFilter = true) {
  const windowStart = issueAfter || CONFIG.issueAfter;
  const url = new URL(CONFIG.endpoint);
  const where = `issue_date > '${windowStart}' and reported_cost > ${CONFIG.minReportedCost}`;
  url.searchParams.set("$where", where);
  url.searchParams.set("$order", "issue_date DESC");
  url.searchParams.set("$limit", String(CONFIG.limit));

  const headers = { Accept: "application/json" };
  if (CONFIG.appToken) {
    headers["X-App-Token"] = CONFIG.appToken;
  }

  const response = await fetch(url, { headers });
  if (!response.ok) {
    throw new Error(`Chicago API request failed (${response.status} ${response.statusText})`);
  }

  const rows = await response.json();
  if (!Array.isArray(rows)) {
    throw new Error("Unexpected response from Chicago API; expected an array.");
  }

  const candidates = useKeywordFilter ? rows.filter(isRestaurantRetail) : rows;
  const filtered = candidates.map(normalizeRecord);

  console.info(`Fetched ${rows.length} rows from ${windowStart}; matched ${filtered.length} ${useKeywordFilter ? "restaurant/retail" : "permit"} candidates.`);

  const deduped = Array.from(new Map(filtered.map((row) => [row.id, row])).values());
  if (deduped.length !== filtered.length) {
    console.info(`De-duplicated ${filtered.length - deduped.length} duplicate records.`);
  }

  return {
    rows: rows.length,
    filtered: deduped.length,
    records: deduped,
    issueAfter: windowStart
  };
}

async function writeJSON(fileName, data) {
  await fs.mkdir(path.dirname(fileName), { recursive: true });
  await fs.writeFile(fileName, JSON.stringify(data, null, 2), "utf8");
}

async function writeHistorySnapshot(bundle) {
  const date = new Date().toISOString().slice(0, 10);
  const fileName = path.join(DATA_DIR, "history", `${date}.json`);
  await writeJSON(fileName, {
    runAt: RUN_AT,
    source: bundle.source,
    opportunities: bundle.opportunities,
    stats: bundle.stats
  });
}

async function main() {
  const output = {
    generatedAt: RUN_AT,
    version: 1,
    source: {
      endpoint: CONFIG.endpoint,
      issueAfter: CONFIG.issueAfter,
      permitTypes: CONFIG.permittedTypes,
      cityKeywordFilter: CONFIG.cityAreaKeywords,
      limit: CONFIG.limit,
      mode: "mock-free prototype"
    },
    stats: {
      fetchedRows: 0,
      filteredRows: 0,
      scoredRows: 0,
      model: CONFIG.modelCandidates[0],
      pilotStart: new Date().toISOString()
    },
    opportunities: []
  };

  const candidates = [
    CONFIG.issueAfter,
    "2025-01-01T00:00:00",
    "2024-01-01T00:00:00",
    "2023-01-01T00:00:00"
  ];

  let fetchResult = null;
  for (const windowStart of candidates) {
    const result = await fetchAndNormalizeRecords(windowStart, true);
    if (result.filtered > 0) {
      fetchResult = result;
      break;
    }
    console.warn(`No qualifying records with issue_date > ${windowStart}; widening window.`);
  }

  if (!fetchResult || fetchResult.filtered === 0) {
    console.warn("No filtered records matched the current keyword strategy. Falling back to latest permit rows so the demo still runs for local evaluation.");
    const fallback = await fetchAndNormalizeRecords(CONFIG.issueAfter, false);
    if (fallback.rows > 0 && fallback.filtered > 0) {
      fetchResult = fallback;
      output.source.mode = "fallback";
      output.source.note = "Keyword filter returned no candidates; using latest permit rows for local continuity.";
    }
  }

  if (!fetchResult || fetchResult.filtered === 0) {
    throw new Error("No qualifying restaurant/retail records found for the available windows.");
  }

  output.stats.fetchedRows = fetchResult.rows;
  output.stats.filteredRows = fetchResult.filtered;
  output.source.issueAfter = fetchResult.issueAfter;

  const top = fetchResult.records
    .sort((a, b) => (parseDate(b.raw.rawDate)?.valueOf() || 0) - (parseDate(a.raw.rawDate)?.valueOf() || 0))
    .slice(0, CONFIG.targetCount);

  const hasAnthropicKey = Boolean(process.env.ANTHROPIC_API_KEY);
  const anthropic = hasAnthropicKey ? new Anthropic({ apiKey: process.env.ANTHROPIC_API_KEY }) : null;
  if (!hasAnthropicKey) {
    console.warn("ANTHROPIC_API_KEY not set. Scoring will use deterministic fallback heuristics.");
  }

  const opportunities = [];
  for (const record of top) {
    const scored = await scoreRecord(record, anthropic);
    opportunities.push({
      id: record.id,
      addr: record.addr,
      hood: record.hood,
      type: record.type,
      score: scored.score,
      rec: scored.rec,
      cost: record.cost,
      sqft: record.sqft,
      filed: record.filed,
      filedDate: record.filedDate,
      status: record.status,
      desc: record.desc,
      owner: record.owner,
      brand: record.brand,
      contractor: record.contractor,
      arch: record.arch,
      reasons: scored.reasons,
      actions: buildActions(record),
      tl: buildTimeline(record, scored),
      scoreModel: scored.model || "heuristic",
      source: {
        permitType: record.raw.permitType,
        permitStatus: record.raw.permitStatus,
        rawId: record.raw.application,
        rawUrl: `${CONFIG.endpoint}?permit_=${encodeURIComponent(record.raw.application || "")}`,
        communityArea: record.raw.communityArea,
        ward: record.raw.ward
      }
    });
  }

  output.stats.scoredRows = opportunities.length;
  output.stats.model = opportunities[0]?.scoreModel || CONFIG.modelCandidates[0];
  output.opportunities = opportunities;

  await writeJSON(path.join(DATA_DIR, "permits.json"), output);
  await writeHistorySnapshot(output);

  console.log(`Wrote ${output.opportunities.length} opportunities to data/permits.json`);
}

main().catch((error) => {
  console.error("Failed to fetch and score permits:", error.message || error);
  process.exit(1);
});
