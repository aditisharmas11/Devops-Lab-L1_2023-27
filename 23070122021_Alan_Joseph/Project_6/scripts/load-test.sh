#!/usr/bin/env bash
set -euo pipefail
# Starts a pod that continuously calls the CPU-heavy endpoint through the service.
kubectl delete pod load-gen -n autoscale-demo --ignore-not-found
kubectl run load-gen -n autoscale-demo --image=busybox:1.36 --restart=Never -- \
  /bin/sh -c "while true; do wget -q -O- http://flask-app/cpu?n=500000 >/dev/null; done"
echo "Load generator started. Watch scaling with: kubectl get hpa -n autoscale-demo -w"
