#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
docker build -t apache2-k8s:1.0 .
minikube image load apache2-k8s:1.0
kubectl apply -k k8s/
kubectl rollout status deployment/apache-deployment -n apache-demo --timeout=120s
