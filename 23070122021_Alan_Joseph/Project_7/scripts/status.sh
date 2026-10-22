#!/usr/bin/env bash
set -euo pipefail
kubectl get deployments,pods,services,configmaps,secrets -n mongo-demo
