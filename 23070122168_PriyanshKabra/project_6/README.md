# Project 6 - Kubernetes Autoscaling

## Objective
Deploy a containerized application on Kubernetes and demonstrate Horizontal Pod Autoscaling (HPA) based on CPU utilization.

## Kubernetes Resources
- Deployment: social-media-app
- Service: social-media-service
- HorizontalPodAutoscaler: social-media-hpa
- Minimum replicas: 2
- Maximum replicas: 5
- CPU target utilization: 50%

## Verification
Kubernetes cluster and application resources were verified using kubectl commands including get nodes, get deployments, get pods, get svc, get hpa, and top pods.

Metrics Server was configured for the Docker Desktop Kubernetes environment using --kubelet-insecure-tls because the kubelet certificate could not be validated against the node IP.

## Autoscaling Demonstration
Under CPU load, the HPA scaled the application from 2 replicas to 5 replicas.
After the CPU load was stopped, the HPA scaled the application back down from 5 replicas to 2 replicas.

## Evidence
1. 01_kubernetes_node_ready.png
2. 02_kubernetes_resources_deployed.png
3. 03_hpa_autoscaling_success.png

## Kubernetes Manifest
The Kubernetes configuration is available at k8s/app.yaml.
