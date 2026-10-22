#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
kubectl apply -k k8s/
for d in user-service product-service order-service api-gateway; do
  kubectl rollout status deployment/$d -n microservices-demo --timeout=120s
done
