@"
# Project 6 - Social Media Infrastructure with Kubernetes

## Objective
Demonstrate application scalability using Kubernetes by creating a cluster and configuring Horizontal Pod Autoscaling (HPA).

## Tools Used
- Kubernetes
- Minikube
- kubectl
- Docker
- Docker Hub
- Spring Boot
- Metrics Server

## Application
Docker image used:

dikas/retail-app:1.1

## Kubernetes Components

### Deployment
The application is deployed using a Kubernetes Deployment with an initial replica count of 2.

### Service
A NodePort Service exposes the Spring Boot application outside the Kubernetes cluster.

### Horizontal Pod Autoscaler
HPA is configured with:
- Minimum replicas: 2
- Maximum replicas: 5
- Target CPU utilization: 50%

## Autoscaling Demonstration

The application initially ran with 2 replicas.

When CPU utilization increased above the 50% target, Kubernetes automatically scaled the application up to 5 replicas.

After the CPU load was stopped, CPU utilization decreased and Kubernetes automatically scaled the application back down to 2 replicas.

## Verification

The following Kubernetes commands were used:

```text
kubectl get deployments
kubectl get pods
kubectl get services
kubectl get hpa
kubectl top pods
minikube service retail-app-service --url