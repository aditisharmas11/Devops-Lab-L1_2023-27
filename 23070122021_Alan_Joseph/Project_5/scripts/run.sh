#!/usr/bin/env bash
set -euo pipefail
docker rm -f retail-app >/dev/null 2>&1 || true
docker run -d --name retail-app -p 8080:8080 retail-app:1.0
echo "Running at http://localhost:8080"
