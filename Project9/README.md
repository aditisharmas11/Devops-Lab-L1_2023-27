# Project 9: Apache2 Server & Host Access

This project demonstrates how to deploy an Apache web server (`httpd`) inside a Kubernetes cluster and access it directly from your host machine (your laptop) using Kubernetes command-line techniques.

## Deployment Instructions

1. Open a terminal in the `Project9` folder.
2. Apply the configuration file to spin up the Apache server:
   ```bash
   kubectl apply -f apache-deployment.yaml
   ```
3. Verify that the pod is running:
   ```bash
   kubectl get pods
   ```

## How to Access it from the Host Machine

There are two main commands you learn in Kubernetes to access an internal service from your host machine. You can use either one for your project screenshots!

### Method 1: Using `kubectl port-forward` (The Command Way)
This is the most common command used by developers to temporarily tunnel into a cluster and view a web server on their host machine.

1. Run this command in your terminal:
   ```bash
   kubectl port-forward service/apache-service 8080:80
   ```
2. Open your web browser and go to **[http://localhost:8080](http://localhost:8080)**.
3. You should see the default Apache **"It works!"** page. 
4. *(Take a screenshot of your browser and the terminal running the port-forward command)*.
5. Press `Ctrl+C` in your terminal to stop the port-forward when you are done.

### Method 2: Using the NodePort (The Service Way)
In our YAML file, we exposed the service using a `NodePort` on port `30080`. Docker Desktop automatically maps this to your localhost.

1. Without running any extra terminal commands, just open your browser and go to **[http://localhost:30080](http://localhost:30080)**.
2. You will see the **"It works!"** page!

## Cleanup
When you are finished taking your screenshots, delete the deployment to save resources:
```bash
kubectl delete -f apache-deployment.yaml
```
