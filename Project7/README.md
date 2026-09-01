# Project 7: MongoDB & Mongo Express on Kubernetes

This project demonstrates how to decouple configuration from application code in Kubernetes using **ConfigMaps** and **Secrets**. We deploy a MongoDB database alongside a web-based database viewer (Mongo Express).

## Architecture
- **Secret**: Stores the sensitive MongoDB admin username and password.
- **ConfigMap**: Stores the non-sensitive internal database URL.
- **MongoDB Deployment & Service**: The backend database server.
- **Mongo Express Deployment & Service**: The frontend web interface that pulls credentials and URL from the Secret and ConfigMap to connect to the database.

## How to Deploy and Test

1. Apply the Secret and ConfigMap *first* (so the pods can use them when they start):
   ```bash
   kubectl apply -f mongo-secret.yaml
   kubectl apply -f mongo-configmap.yaml
   ```

2. Apply the Deployments and Services:
   ```bash
   kubectl apply -f mongo-deployment.yaml
   kubectl apply -f mongo-express-deployment.yaml
   ```

3. Verify everything is running:
   ```bash
   kubectl get pods
   kubectl get service
   ```

4. **Test the Application**: 
   Since we used a `LoadBalancer` service type for Mongo Express, Docker Desktop will automatically expose it to your localhost.
   Open your browser and navigate to: **http://localhost:8081**
   
   *(You should see the Mongo Express dashboard showing the internal MongoDB databases!)*

5. **Clean up**:
   ```bash
   kubectl delete -f mongo-express-deployment.yaml
   kubectl delete -f mongo-deployment.yaml
   kubectl delete -f mongo-configmap.yaml
   kubectl delete -f mongo-secret.yaml
   ```
