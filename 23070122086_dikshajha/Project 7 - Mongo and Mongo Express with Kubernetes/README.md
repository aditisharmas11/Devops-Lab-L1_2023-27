# Project 7 - Mongo and Mongo Express with Kubernetes

## Objective

To deploy MongoDB and Mongo Express using Kubernetes and demonstrate the use of Deployments, Services, ConfigMap and Secret.

## Tools Used

* Kubernetes
* Minikube
* kubectl
* Docker Desktop
* MongoDB
* Mongo Express

## Kubernetes Components

The project contains:

* MongoDB Deployment
* MongoDB Service
* MongoDB ConfigMap
* MongoDB Secret
* Mongo Express Deployment
* Mongo Express Service

## MongoDB Deployment

A Kubernetes Deployment named `mongo` was created with one MongoDB replica using the `mongo:7` image.

MongoDB uses port `27017`.

The MongoDB root username and password are provided through the Kubernetes Secret.

## MongoDB Service

The `mongo-service` Service exposes MongoDB inside the Kubernetes cluster on port `27017`.

It uses the `ClusterIP` service type.

## MongoDB ConfigMap

The `mongo-configmap` ConfigMap stores non-sensitive MongoDB connection information:

* MongoDB host: `mongo-service`
* MongoDB port: `27017`

## MongoDB Secret

The `mongo-secret` Kubernetes Secret stores sensitive MongoDB credentials.

The credentials are not exposed in this README.

## Mongo Express Deployment

A Kubernetes Deployment named `mongo-express` was created with one replica using the `mongo-express:1.0.2` image.

Mongo Express uses port `8081`.

The MongoDB server and port are obtained from the ConfigMap, while the MongoDB credentials are obtained from the Secret.

## Mongo Express Service

The `mongo-express-service` Service exposes Mongo Express using the `NodePort` service type.

Mongo Express is available on port `8081`.

## How the Components Communicate

The architecture is:

Browser
↓
Mongo Express Service
↓
Mongo Express Pod
↓
MongoDB Service
↓
MongoDB Pod

The Mongo Express Deployment uses `mongo-service` as the MongoDB hostname.

## Commands Used

```bash
minikube start --driver=docker

kubectl apply -f ./kubernetes/

kubectl get deployments
kubectl get pods
kubectl get services
kubectl get configmaps
kubectl get secrets

minikube service mongo-express-service --url
```

## Verification

The following results were successfully verified:

* MongoDB Deployment: `1/1 Ready`
* Mongo Express Deployment: `1/1 Ready`
* MongoDB Pod: `Running`
* Mongo Express Pod: `Running`
* MongoDB Service: `ClusterIP`
* Mongo Express Service: `NodePort`
* MongoDB ConfigMap: created
* MongoDB Secret: created
* Mongo Express web interface: successfully accessed

## Result

MongoDB and Mongo Express were successfully deployed and connected using Kubernetes.

The project demonstrates Kubernetes Deployments, Services, ConfigMap, Secret and communication between Mongo Express and MongoDB.

## Screenshots

The `Screenshots` folder contains evidence of:

1. MongoDB and Mongo Express Pods
2. MongoDB and Mongo Express Services
3. ConfigMap and Secret
4. Mongo Express web application
5. Final Kubernetes status
