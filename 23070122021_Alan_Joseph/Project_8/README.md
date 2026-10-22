# Project 8 - Microservices Application on Kubernetes

A small retail system split into four services, each with its own image, Deployment and Service:

| Service | Port | Purpose |
|---|---|---|
| api-gateway | 5000 (NodePort 30080) | Single entry point, checks the API key, routes `/api/*` |
| user-service | 5001 | `GET /users`, `GET /users/<id>` |
| product-service | 5002 | `GET /products`, `GET /products/<id>` |
| order-service | 5003 | `GET /orders`, `POST /orders` (calls user and product services) |

ConfigMap holds the service URLs. Secret holds the gateway API key.

## Deploy
```bash
scripts/build-images.sh   # builds the four images and loads them into minikube
scripts/deploy.sh         # applies the manifests
scripts/status.sh
scripts/test.sh           # runs end-to-end requests through the gateway
```

## Manual check
```bash
GW=$(minikube service api-gateway -n microservices-demo --url)
curl -H "X-API-Key: lab-api-key" $GW/api/products
curl -H "X-API-Key: lab-api-key" -X POST -H "Content-Type: application/json" \
     -d '{"user_id":1,"product_id":2,"quantity":2}' $GW/api/orders
```

## Clean up
```bash
scripts/cleanup.sh
```
