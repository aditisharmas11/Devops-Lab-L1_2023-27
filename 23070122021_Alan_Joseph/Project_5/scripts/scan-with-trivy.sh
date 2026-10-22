#!/usr/bin/env bash
set -euo pipefail
# Runs Trivy from its official container. Fails (exit 1) if HIGH or CRITICAL CVEs are found.
docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy:latest image \
  --severity HIGH,CRITICAL \
  --exit-code 1 \
  retail-app:1.0
