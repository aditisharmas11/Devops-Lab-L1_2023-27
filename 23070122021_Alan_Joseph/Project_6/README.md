# Project 6 - Scalable App on Kubernetes with Horizontal Pod Autoscaling

A Flask app runs in Kubernetes with a HorizontalPodAutoscaler (HPA). Under CPU load the HPA adds pods; when load drops it removes them.

## Prerequisites
Docker, minikube, kubectl.

## Steps
```bash
scripts/start-minikube.sh   # starts minikube and enables metrics-server
scripts/deploy.sh           # builds the image, loads it into minikube, applies manifests
scripts/load-test.sh        # starts a load generator pod hitting /cpu
kubectl get hpa -n autoscale-demo -w     # watch replicas grow
scripts/cleanup.sh          # remove everything
```

Open the app:
```bash
minikube service flask-app -n autoscale-demo --url
```

## Files
- `app/` - Flask app and Dockerfile (`/` info, `/cpu` CPU-heavy work, `/healthz`)
- `k8s/` - namespace, deployment, service, HPA and kustomization
- `scripts/` - minikube start, deploy, load test and cleanup
