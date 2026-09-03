# Project 8 - Microservices on Kubernetes

## Objective
Deploy a multi-service application on Kubernetes using separate Deployments and Services.

## Microservices
- frontend
- users-service
- products-service
- orders-service

## Kubernetes Resources
- ConfigMap: app-config
- Secret: app-secret
- Deployments: frontend, users-service, products-service, orders-service
- Services: frontend-service, users-service, products-service, orders-service

## Verification
All four microservice deployments reached Ready status and their pods were Running successfully.

The frontend was accessed through Kubernetes port forwarding at localhost:8083 because direct NodePort access was unavailable in the Docker Desktop environment.

## Evidence
1. 01_microservices_kubernetes.png - Frontend successfully accessed
2. 02_microservices_k8s_resources.png - Kubernetes resources

## Manifest
k8s/microservices.yaml
