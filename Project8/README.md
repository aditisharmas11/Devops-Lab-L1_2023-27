# Project 8: Complete Microservice Architecture

This project containerizes a complete e-commerce application broken down into **4 distinct microservices**.

## Architecture Overview
1. **Frontend Service**: An Nginx web server acting as the user-facing interface. (Exposed on port 80 via `LoadBalancer`).
2. **Product API**: A backend service that returns product catalog data.
3. **User API**: A backend service that handles user authentication.
4. **User Database**: A PostgreSQL database container that stores the user data for the User API.

## Configuration & Security
- **ConfigMap (`02-configmaps.yaml`)**: Stores internal URLs (e.g., `http://product-api-service:8080`) so the microservices know how to talk to each other inside the cluster.
- **Secret (`01-secrets.yaml`)**: Securely stores the PostgreSQL database password so it is not hardcoded in the deployment files.

## Deployment Instructions

1. Open a terminal in this `Project8` folder.
2. Apply all the configuration files in order:
   ```bash
   kubectl apply -f 01-secrets.yaml
   kubectl apply -f 02-configmaps.yaml
   kubectl apply -f 03-user-db.yaml
   kubectl apply -f 04-user-api.yaml
   kubectl apply -f 05-product-api.yaml
   kubectl apply -f 06-frontend.yaml
   ```

3. Verify that all 4 microservices are spinning up:
   ```bash
   kubectl get pods
   kubectl get services
   ```

4. Since the `frontend-service` is set to `LoadBalancer`, you can access the entry point of the microservice cluster by opening your browser to:
   **[http://localhost](http://localhost)** (or `http://localhost:80` if it requires the port).
