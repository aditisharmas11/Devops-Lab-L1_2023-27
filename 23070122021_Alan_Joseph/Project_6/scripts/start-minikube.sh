#!/usr/bin/env bash
set -euo pipefail
minikube start --cpus=2 --memory=3072
minikube addons enable metrics-server
kubectl get nodes
