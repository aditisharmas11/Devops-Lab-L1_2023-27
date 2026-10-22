#!/usr/bin/env bash
set -euo pipefail
echo "Forwarding http://localhost:8088 -> apache-service:80 (Ctrl+C to stop)"
kubectl port-forward svc/apache-service 8088:80 -n apache-demo
