# Project 9 - Apache HTTP Server on Kubernetes

## Objective

Deploy an Apache HTTP Server container on Kubernetes and expose it using a NodePort Service.

## Kubernetes Resources

- Deployment: apache-server
- Service: apache-service

## Configuration

- Docker image: httpd:2.4
- Replicas: 1
- Container port: 80
- Service port: 80
- NodePort: 30083

## Verification

The Apache deployment was verified using:

- kubectl get deployment apache-server
- kubectl get pods -l app=apache
- kubectl get svc apache-service

The Apache pod reached Running/Ready status.

The application was accessed through Kubernetes port forwarding at:

http://localhost:8084

The browser displayed the Apache "It works!" page successfully.

## Evidence

1. 01_apache2_kubernetes.png - Apache web page accessed successfully
2. 02_apache2_k8s_resources.png - Apache Kubernetes resources

## Kubernetes Manifest

The complete Kubernetes configuration is available at:

k8s/apache.yaml