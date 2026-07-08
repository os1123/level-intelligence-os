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

# Include the live demo page in the published bundle.
if [[ -f "${ROOT}/level-intelligence-os-demo.html" ]]; then
  cp "${ROOT}/level-intelligence-os-demo.html" "${OUTPUT_DIR}/"
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
