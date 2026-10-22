#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
kubectl apply -k k8s/
kubectl rollout status deployment/mongodb -n mongo-demo --timeout=180s
kubectl rollout status deployment/mongo-express -n mongo-demo --timeout=180s
