#!/usr/bin/env bash
set -euo pipefail
kubectl get pods,svc -n apache-demo -o wide
POD=$(kubectl get pod -n apache-demo -l app=apache -o jsonpath='{.items[0].metadata.name}')
echo "--- Apache version inside $POD"
kubectl exec "$POD" -n apache-demo -- apache2 -v
