#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")/.."
kubectl delete pod load-gen -n autoscale-demo --ignore-not-found
kubectl delete -k k8s/ --ignore-not-found
echo "Cleaned up. (minikube itself is still running; use 'minikube stop' to stop it.)"
