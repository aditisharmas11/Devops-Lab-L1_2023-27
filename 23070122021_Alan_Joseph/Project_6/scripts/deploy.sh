#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
docker build -t flask-autoscale:1.0 app/
minikube image load flask-autoscale:1.0
kubectl apply -k k8s/
kubectl rollout status deployment/flask-app -n autoscale-demo --timeout=120s
echo "App URL: $(minikube service flask-app -n autoscale-demo --url)"
