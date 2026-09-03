# Project 7 - MongoDB and Mongo Express on Kubernetes

## Objective
Deploy MongoDB and Mongo Express on Kubernetes using Deployments, Services, ConfigMap, and Secret.

## Kubernetes Resources
- ConfigMap: mongo-config
- Secret: mongo-secret
- MongoDB Deployment: mongo
- MongoDB Service: mongo-service
- Mongo Express Deployment: mongo-express
- Mongo Express Service: mongo-express-service

## Configuration
- MongoDB image: mongo:7
- Mongo Express image: mongo-express:1.0.2
- MongoDB port: 27017
- Mongo Express port: 8081
- NodePort: 30081

## Verification
The application was verified using kubectl commands including get deployments, get pods, get svc, get configmap, and get secret.

Both MongoDB and Mongo Express reached Running/Ready status.
Mongo Express was accessed through the Kubernetes service using port forwarding.

## Evidence
1. 01_mongo_express.png - Mongo Express web interface
2. 02_mongo_k8s_resources.png - Kubernetes resources

## Kubernetes Manifest
The complete Kubernetes configuration is available at k8s/mongo-mongoexpress.yaml.