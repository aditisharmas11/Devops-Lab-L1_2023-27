# Project 6 — Social media infra: Kubernetes cluster + HPA

**Student:** Arsh Ansari | **PRN:** 23070122047

Kind cluster `devops-lab` plus a CPU-burning social-feed API. Horizontal Pod Autoscaler scales **1–6** replicas at **50%** average CPU.

## Cluster

```powershell
$env:PATH = "$env:USERPROFILE\bin;$env:PATH"
kind create cluster --config ..\kind-cluster.yaml
kubectl apply -f ..\metrics-server.yaml
```

## App

```powershell
docker build -t social-feed:1.0.0 .
kind load docker-image social-feed:1.0.0 --name devops-lab
kubectl apply -f k8s.yaml
```

NodePort **30080**. `/feed` hashes in a tight loop so metrics-server sees CPU and HPA scales up.

```powershell
kubectl get hpa social-feed --watch
# from another terminal:
for ($i=0; $i -lt 200; $i++) { curl -s http://localhost:30080/feed | Out-Null }
```

---

## Evidence

![Pods and HPA](./screenshots/01-hpa.txt)
![Load and replica scale](./screenshots/02-scale.txt)
