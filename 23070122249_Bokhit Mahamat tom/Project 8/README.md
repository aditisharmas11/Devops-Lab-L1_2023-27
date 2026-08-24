# ShopEase — Kubernetes Microservices Deployment

A complete Kubernetes manifest set for a containerized e-commerce app with
**4 microservices** plus a shared database, demonstrating Deployments,
Services, ConfigMaps, and Secrets working together.

## Architecture

```
                        ┌─────────────┐
   Internet ───────────▶│  frontend   │  (nginx, LoadBalancer Service)
                        └──────┬──────┘
                               │ reverse-proxies /api/*
        ┌──────────────────────┼──────────────────────┐
        ▼                      ▼                       ▼
 ┌─────────────┐      ┌─────────────────┐      ┌───────────────┐
 │ user-service │      │ product-service │      │ order-service │
 │  (:3001)     │      │    (:3002)      │      │   (:3003)     │
 └──────┬───────┘      └────────┬────────┘      └───────┬───────┘
        │                       │                        │
        └───────────────────────┼────────────────────────┘
                                 ▼
                          ┌─────────────┐
                          │  postgres   │  (users_db / products_db / orders_db)
                          └─────────────┘
```

Each backend service is stateless and independently scalable; Postgres
holds three logically-separated databases (one per service) so each
microservice still "owns" its own data.

## Files

| File | Kind(s) | Purpose |
|---|---|---|
| `00-namespace.yaml` | Namespace | Isolates all resources under `shopease` |
| `01-configmaps.yaml` | ConfigMap ×3 | Shared env vars, frontend nginx config, Postgres init SQL |
| `02-secrets.yaml` | Secret ×4 | DB credentials, per-service DB URLs, JWT key, payment API key |
| `03-postgres.yaml` | Deployment, Service, PVC | Shared Postgres instance |
| `04-user-service.yaml` | Deployment, Service | Auth & user profiles |
| `05-product-service.yaml` | Deployment, Service | Product catalog |
| `06-order-service.yaml` | Deployment, Service | Orders & checkout |
| `07-frontend.yaml` | Deployment, Service | Web UI (nginx), public entrypoint |

## Before you deploy

1. **Build and push your own images**, then update the `image:` field in
   `04-`, `05-`, `06-`, `07-*.yaml` (currently placeholders like
   `your-registry/user-service:1.0.0`). Each backend service is expected to
   expose a `GET /health` endpoint (used by readiness/liveness probes).
2. **Replace secret values** in `02-secrets.yaml` — the passwords/keys in
   there are placeholders. For real deployments, prefer
   `kubectl create secret generic ... --from-literal=...` or a secrets
   manager (Vault, AWS/GCP Secret Manager, Sealed Secrets) over committing
   plaintext YAML to git.
3. If you're on a local cluster (minikube/kind), change the `frontend`
   Service `type` from `LoadBalancer` to `NodePort` in `07-frontend.yaml`.

## Deploy

Apply in order (namespace and config first, since Deployments reference them):

```bash
kubectl apply -f 00-namespace.yaml
kubectl apply -f 01-configmaps.yaml
kubectl apply -f 02-secrets.yaml
kubectl apply -f 03-postgres.yaml
kubectl apply -f 04-user-service.yaml
kubectl apply -f 05-product-service.yaml
kubectl apply -f 06-order-service.yaml
kubectl apply -f 07-frontend.yaml
```

Or apply the whole directory at once — `kubectl` sorts out most ordering
issues on its own, and will simply retry pods that start before their
dependencies are ready:

```bash
kubectl apply -f .
```

## Verify

```bash
kubectl get all -n shopease
kubectl get configmaps,secrets -n shopease
kubectl rollout status deployment/user-service -n shopease
kubectl logs -n shopease deployment/order-service
```

Get the frontend's external address:

```bash
kubectl get svc frontend -n shopease
```

## Scaling

```bash
kubectl scale deployment/product-service --replicas=4 -n shopease
```

## Cleanup

```bash
kubectl delete namespace shopease
```
(Deletes every resource above in one shot, since they all live in the
`shopease` namespace.)

## Notes on design choices

- **ConfigMaps vs Secrets**: non-sensitive shared config (log level, internal
  service URLs) lives in ConfigMaps; credentials and API keys live in
  Secrets. Services consume both via `envFrom`, so adding a new config key
  doesn't require touching the Deployment spec.
- **Per-service DB creds**: each backend has its own `DATABASE_URL` secret
  scoped to its own database, following least-privilege / data-ownership
  principles even though they share one Postgres instance.
- **Probes**: every container has readiness and liveness probes so
  Kubernetes won't route traffic to a service before it's ready, and will
  restart it if it hangs.
- **Resource requests/limits**: set conservatively on every container so the
  scheduler can bin-pack correctly and one runaway service can't starve the
  others.
