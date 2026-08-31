# Project 8 — Four microservices on Kubernetes

**Student:** Arsh Ansari | **PRN:** 23070122047

Complete store stack with **four** services, plus a shared ConfigMap and Secret.

| Workload | Image | Role |
|----------|-------|------|
| `user-service` | `store-service:1.0.0` | Users |
| `product-service` | `store-service:1.0.0` | Catalog |
| `order-service` | `store-service:1.0.0` | Orders |
| `frontend-gateway` | `store-gateway:1.0.0` | Aggregates the three APIs, NodePort **30082** |

`store-config` holds `USER_URL`, `PRODUCT_URL`, `ORDER_URL`. `store-secret` holds `API_KEY`.

```powershell
docker build -t store-service:1.0.0 services
docker build -t store-gateway:1.0.0 gateway
kind load docker-image store-service:1.0.0 store-gateway:1.0.0 --name devops-lab
kubectl apply -f k8s.yaml
curl http://localhost:30082/
```

---

## Evidence

![Deployments and services](./screenshots/01-kubectl.txt)
![Gateway JSON](./screenshots/02-gateway.txt)
