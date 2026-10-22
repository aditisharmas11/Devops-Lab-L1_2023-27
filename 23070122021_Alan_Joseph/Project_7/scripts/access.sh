#!/usr/bin/env bash
set -euo pipefail
echo "Mongo Express: $(minikube service mongo-express-service -n mongo-demo --url)"
