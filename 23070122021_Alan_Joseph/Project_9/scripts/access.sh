#!/usr/bin/env bash
set -euo pipefail
echo "NodePort URL: $(minikube service apache-service -n apache-demo --url)"
