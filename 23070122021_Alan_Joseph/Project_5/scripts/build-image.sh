#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
docker build -t retail-app:1.0 .
echo "Built retail-app:1.0"
