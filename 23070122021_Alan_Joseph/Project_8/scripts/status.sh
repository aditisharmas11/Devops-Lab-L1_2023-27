#!/usr/bin/env bash
set -euo pipefail
kubectl get deployments,pods,services,configmaps -n microservices-demo
