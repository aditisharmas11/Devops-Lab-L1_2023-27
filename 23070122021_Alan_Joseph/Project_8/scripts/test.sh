#!/usr/bin/env bash
set -euo pipefail
GW=$(minikube service api-gateway -n microservices-demo --url)
KEY=lab-api-key
echo "--- products"
curl -s -H "X-API-Key: $KEY" "$GW/api/products"; echo
echo "--- create order"
curl -s -H "X-API-Key: $KEY" -H "Content-Type: application/json" \
     -X POST -d '{"user_id":1,"product_id":2,"quantity":2}' "$GW/api/orders"; echo
echo "--- orders"
curl -s -H "X-API-Key: $KEY" "$GW/api/orders"; echo
echo "--- no key (expect 401)"
curl -s -o /dev/null -w "%{http_code}\n" "$GW/api/products"
