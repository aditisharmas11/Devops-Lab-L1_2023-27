# Project 6: Social Media Infrastructure Scalability

This project demonstrates how to set up Kubernetes **Horizontal Pod Autoscaling (HPA)** to solve application scalability challenges for a Social Media platform. 

When a social media post goes viral, the server experiences a massive spike in traffic. Kubernetes HPA monitors this CPU usage and automatically creates more pods (servers) to handle the load, and then scales them back down when traffic decreases.

## Requirements
- Kubernetes Cluster (Docker Desktop with Kubernetes enabled, Minikube, or a Cloud Provider).
- `kubectl` command-line tool installed and configured.
- A **Metrics Server** running in the cluster (HPA requires this to read CPU metrics).

## Instructions

### Step 1: Deploy the Application
We will deploy our social media app (using an image designed to consume CPU when requested) and its service.
```bash
kubectl apply -f social-media-deployment.yaml
```

### Step 2: Deploy the Autoscaler (HPA)
Deploy the Horizontal Pod Autoscaler. It is configured to scale up the pods (max 10) if the CPU utilization goes over 50%.
```bash
kubectl apply -f social-media-hpa.yaml
```

### Step 3: Verify Setup
Check if the HPA is successfully tracking your deployment's metrics:
```bash
kubectl get hpa
```
*Note: It may say `<unknown>/50%` for a minute or two until the metrics server collects the data. Once it says `0%/50%`, it is ready!*

## Testing the Autoscale Feature
To prove that the autoscaler works, we need to simulate a massive traffic spike (like a viral social media post).

1. **Open a new terminal window** and run a continuous loop of traffic to the service:
   ```bash
   kubectl run -i --tty load-generator --rm --image=busybox:1.28 --restart=Never -- /bin/sh -c "while sleep 0.01; do wget -q -O- http://social-media-service; done"
   ```
2. **Go back to your first terminal window** and watch the HPA react to the traffic:
   ```bash
   kubectl get hpa -w
   ```
3. Within a few minutes, you will see the CPU utilization spike (e.g., `250%/50%`). 
4. Check your pods, and you will see Kubernetes automatically creating new ones to handle the load!
   ```bash
   kubectl get deployment social-media-app
   ```
5. **Stop the load generator** by pressing `Ctrl+C` in that terminal. Within 5-10 minutes, Kubernetes will automatically scale the pods back down to 1.
