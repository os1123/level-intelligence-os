#!/usr/bin/env bash

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
OUTPUT_DIR="${ROOT}/share-site"
SOURCE_DIR="${ROOT}/publish"
DATA_DIR="${ROOT}/data"

rm -rf "${OUTPUT_DIR}"
mkdir -p "${OUTPUT_DIR}"

# Copy all web-facing assets from publish/
cp -R "${SOURCE_DIR}/." "${OUTPUT_DIR}/"

# The checked-in publish page lives under /publish/ for legacy Pages, where
# ../level-... points back to the repo root. The generated share-site bundle
# serves index.html at its own root, so normalize those demo links there.
if [[ -f "${OUTPUT_DIR}/index.html" ]]; then
  perl -0pi -e 's#href="\.\./level-intelligence-os-#href="level-intelligence-os-#g' "${OUTPUT_DIR}/index.html"
fi

# Include the live demo page in the published bundle.
if [[ -f "${ROOT}/level-intelligence-os-demo.html" ]]; then
  cp "${ROOT}/level-intelligence-os-demo.html" "${OUTPUT_DIR}/"
fi

# Include the agent operations visualization in the published bundle.
if [[ -f "${ROOT}/level-intelligence-os-agent-ops.html" ]]; then
  cp "${ROOT}/level-intelligence-os-agent-ops.html" "${OUTPUT_DIR}/"
fi

# Add fetched data for the demo page only when available.
mkdir -p "${OUTPUT_DIR}/data"
if [[ -f "${DATA_DIR}/permits.json" ]]; then
  cp "${DATA_DIR}/permits.json" "${OUTPUT_DIR}/data/"
fi

if [[ -d "${DATA_DIR}/history" ]]; then
  mkdir -p "${OUTPUT_DIR}/data/history"
  cp "${DATA_DIR}/history/"*.json "${OUTPUT_DIR}/data/history/" 2>/dev/null || true
fi

echo "Built share site at ${OUTPUT_DIR}"
