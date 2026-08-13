# Kubernetes HPA Demo (Project 6)

This repository demonstrates Kubernetes Horizontal Pod Autoscaling (HPA) using a simple NGINX deployment. The application is exposed through an internal Service, and an autoscaler watches CPU utilization to scale the Deployment up or down automatically.

## Architecture

```text
Client / load generator
        |
        v
    Service (ClusterIP)
        |
        v
  Deployment (nginx)
        |
        v
  Replica Pods
        |
        v
       HPA
  (monitors CPU usage)
```

## Files Included

- `deployment.yaml` — NGINX Deployment with CPU and memory requests/limits
- `service.yaml` — Internal Service that routes traffic to the app Pods
- `hpa.yaml` — HPA configured to scale between 2 and 10 replicas
- `load-test.yaml` — BusyBox pod that sends continuous requests to the Service

## Prerequisites

1. Enable Kubernetes in Docker Desktop:

```bash
Docker Desktop -> Settings -> Kubernetes -> Enable Kubernetes
```

2. Make sure `kubectl` is connected to the correct cluster:

```bash
kubectl version --client
kubectl get nodes
```

If `kubectl get nodes` points to the wrong context or returns auth errors, switch to Docker Desktop:

```bash
kubectl config get-contexts
kubectl config use-context docker-desktop
kubectl get nodes
```

3. Ensure the metrics server is running. HPA requires it to read CPU metrics:

```bash
kubectl top nodes
kubectl top pods
```

If metrics are missing, install the metrics server for your cluster before testing HPA.

## Deploy the Application

Apply the manifests:

```bash
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml
kubectl apply -f hpa.yaml
```

Verify the resources:

```bash
kubectl get deployments
kubectl get pods
kubectl get services
kubectl get hpa
```

The Deployment starts with 2 replicas because the HPA `minReplicas` is set to 2.

## Generate Load

Start the synthetic traffic generator:

```bash
kubectl apply -f load-test.yaml
```

Watch the autoscaler and Pods in parallel:

```bash
kubectl get hpa -w
kubectl get pods -w
```

As the CPU load rises, the HPA scales the Deployment to match demand until it reaches the configured maximum of 10 replicas.

## Remove the Load

Stop the load generator:

```bash
kubectl delete -f load-test.yaml
```

Continue watching the HPA:

```bash
kubectl get hpa -w
```

When CPU usage falls, the HPA scales the Deployment back toward the minimum replica count.

## Suggested Lab Evidence Commands

```bash
kubectl get nodes
kubectl get deployments
kubectl get pods
kubectl get svc
kubectl get hpa
kubectl top pods
kubectl apply -f load-test.yaml
kubectl get hpa -w
kubectl get pods -w
kubectl delete -f load-test.yaml
kubectl get hpa
```

## Summary

This project shows how a Kubernetes Deployment can scale automatically with CPU-based HPA rules. With the service and load generator in place, you can observe real-time scaling behavior without any custom application code.
