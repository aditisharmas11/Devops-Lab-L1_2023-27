#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
for svc in api-gateway user-service product-service order-service; do
  docker build -t "$svc:1.0" "services/$svc"
  minikube image load "$svc:1.0"
done
