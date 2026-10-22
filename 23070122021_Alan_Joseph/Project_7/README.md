# Project 7 - MongoDB and Mongo Express on Kubernetes

Deploys MongoDB and its web admin UI (Mongo Express) to Kubernetes using Deployments, Services, ConfigMaps and Secrets.

## Deploy
```bash
scripts/deploy.sh
scripts/status.sh
scripts/access.sh        # prints the Mongo Express URL
```
Mongo Express asks for the basic-auth login defined in `k8s/secret.yaml` (default `admin` / `pass123`, change it before real use).

## Design
- `secret.yaml` - MongoDB root credentials and the Mongo Express basic-auth password
- `configmap.yaml` - non-secret settings (MongoDB host, port, Mongo Express user)
- `mongo-deployment.yaml` + `mongo-service.yaml` - MongoDB, reachable inside the cluster as `mongo-service:27017`
- `mongo-express-deployment.yaml` + `mongo-express-service.yaml` - UI, exposed as NodePort 30081

Data is stored in the container filesystem, so it is lost when the pod is deleted. Add a PersistentVolumeClaim if you need durable storage.

## Clean up
```bash
scripts/cleanup.sh
```
