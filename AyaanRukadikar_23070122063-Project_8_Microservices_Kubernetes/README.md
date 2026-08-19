# Project 8: Deploying a Multi-Tier Microservices-Based E-Commerce Platform on Kubernetes Using Deployments, Services, ConfigMaps, and Secrets

**Student Name:** Ayaan Rukadikar  
**PRN:** 23070122063  
**Subject:** DevOps Lab  
**Batch:** 2023-27  

---

## 1. Executive Summary & Project Overview

Contemporary cloud-native application designs depend on loosely coupled, individually scalable microservices managed through container orchestration platforms such as Kubernetes. Breaking down monolithic enterprise systems into focused domain-specific services enhances team independence, deployment stability, failure containment, and efficient resource usage.

**Project 8** presents a thorough, real-world multi-tier e-commerce ecosystem named **ShopSphere**. The platform consists of four distinct backend microservices alongside an interactive web-based frontend dashboard, all packaged in Docker containers and managed declaratively within a dedicated Kubernetes namespace (`microservices-demo`):
- **Frontend Dashboard:** A responsive, glassmorphic web interface offering real-time microservice health monitoring, product catalog browsing, user directory access, and live order submission.
- **Product Catalog Service:** A high-performance REST API for managing inventory items, pricing data, ratings, and detailed product specifications.
- **User Directory Service:** A microservice handling customer and administrator identity data, including profiles, geographic locations, and role-based access.
- **Order Processing Service:** A transactional engine that executes multi-step order workflows, performing live inter-service RPC calls to validate data against the Product and User services, and emitting event dispatches.
- **Notification & Event Service:** An asynchronous event handler and alert dispatcher that records order confirmations and broadcasts system notifications.

The orchestration layer makes use of essential Kubernetes primitives:
- **Namespaces:** Multi-tenant resource isolation boundary (`microservices-demo`).
- **Deployments:** Declarative replica management with rolling update policies, resource constraints, and HTTP-based liveness/readiness health probes.
- **Services (ClusterIP & NodePort):** Decoupled internal service discovery through Kubernetes CoreDNS (`http://product-service:3000`, `http://user-service:3000`, etc.) combined with external NodePort ingress for browser access.
- **ConfigMaps:** Centralized, externalized environment settings (`APP_ENV`, backend routing URLs, port assignments).
- **Secrets:** Base64-encoded credential storage that protects database passwords and API tokens, eliminating the need to embed sensitive values directly in application source code.

---

## 2. Problem Statement & Business Scenario

In enterprise-grade commerce platforms, combining user management, product catalogs, order processing, and notification workflows into a single monolithic codebase introduces significant failure risks:
1. **Cascading Failures:** An issue in the notification subsystem or excessive traffic during flash sales can take down the entire checkout flow and user authentication layer.
2. **Tightly Coupled Releases:** Even minor catalog schema changes necessitate rebuilding and redeploying the whole application stack.
3. **Embedded Secrets & Configurations:** Monolithic applications often intermingle environment settings and database credentials within source code, creating serious security vulnerabilities and maintenance overhead.

### The DevOps Approach
By containerizing each domain as a self-contained microservice and deploying onto Kubernetes:
- Every service runs within its own isolated container runtime, governed by dedicated CPU and memory limits.
- Services locate one another dynamically via Kubernetes internal DNS entries (`product-service`, `user-service`, `order-service`, `notification-service`).
- Environment configuration values are injected at runtime from a Kubernetes `ConfigMap`.
- Sensitive database and API credentials are securely provisioned through a Kubernetes `Secret`.
- The frontend web layer interacts with all backend services seamlessly over Kubernetes internal networking.

---

## 3. System Architecture & Component Workflow

The ASCII diagram below depicts the multi-tier microservices architecture, showing inter-service communication paths, DNS-based service discovery, and configuration injection within the `microservices-demo` namespace:

```
                                    +-----------------------------------------+
                                    |           Kubernetes Node               |
                                    |                                         |
                                    |   [ ConfigMap: shopsphere-config ]      |
                                    |   - APP_ENV: production                 |
                                    |   - PRODUCT_SERVICE_URL                 |
                                    |   - USER_SERVICE_URL                    |
                                    |   - ORDER_SERVICE_URL                   |
                                    |   - NOTIFICATION_SERVICE_URL            |
                                    |                                         |
                                    |   [ Secret: shopsphere-secret ]         |
                                    |   - DB_USERNAME / DB_PASSWORD           |
                                    |   - API_SECRET                          |
                                    +--------------------+--------------------+
                                                         |
                              +--------------------------v--------------------------+
                              |         Namespace: microservices-demo               |
                              |                                                     |
                              |   +---------------------------------------------+   |
                              |   |          ShopSphere Web Frontend            |   |
                              |   |        (Pod Container Port: 8080)           |   |
                              |   +----------------------┬----------------------+   |
                              |                          |                          |
                              |       ┌──────────────────┼──────────────────┐       |
                              |       │ (ClusterIP DNS)  │ (ClusterIP DNS)  │ (DNS) |
                              |       ▼                  ▼                  ▼       |
                              | +------------+    +------------+    +------------+  |
                              | |  Product   |    |    User    |    |   Order    |  |
                              | |  Service   |    |  Service   |    |  Service   |  |
                              | | (Port 3000)|    | (Port 3000)|    | (Port 3000)|  |
                              | +------------+    +------------+    +-----┬------+  |
                              |       │                  │                │         |
                              |       │                  │ (Inter-Service)│         |
                              |       └──────────────────┴──────────┬─────┘         |
                              |                                     ▼               |
                              |                           +--------------------+    |
                              |                           |Notification Service|    |
                              |                           |    (Port 3000)     |    |
                              |                           +--------------------+    |
                              +-----------------------------------------------------+
                                                         |
                                         frontend-service (NodePort: 30080 / Port-Forward: 8080)
                                                         |
                                                         v
                                              +---------------------+
                                              |  Web Browser / User |
                                              | http://localhost:8080|
                                              +---------------------+
```

### Architectural Highlights
1. **No Hardcoded Endpoints:** Every microservice communicates via Kubernetes CoreDNS (`http://<service-name>:3000`) rather than using `localhost` for inter-service calls.
2. **Externalized Configuration & Credentials:** All environment variables and secrets are managed declaratively using Kubernetes `ConfigMap` and `Secret` resources.
3. **Continuous Health Monitoring:** Each microservice exposes a `/health` endpoint that is actively polled by Kubernetes `livenessProbe` and `readinessProbe` configurations.

---

## 4. Technology Stack

| Layer / Role | Technology / Tool | Version / Spec | Purpose |
| :--- | :--- | :--- | :--- |
| **Container Engine** | Docker Engine / Buildx | v27+ | Building multi-service OCI container images |
| **Container Base** | Node.js Alpine | `node:18-alpine` | Lightweight, secure microservice base image |
| **Backend Services** | Express.js / Node.js | v4.19.2 | High-throughput REST API microservices |
| **Frontend Web UI** | HTML5, Vanilla CSS3, JS | ES6+ | Real-time responsive telemetry and e-commerce UI |
| **Orchestration** | Kubernetes (`kind`) | v1.32.2 | Container deployment, replica control, and self-healing |
| **Configuration** | Kubernetes ConfigMap | `v1/ConfigMap` | Decoupled non-sensitive environment variables |
| **Secret Management**| Kubernetes Secret | `v1/Secret` (Opaque) | Secure database and token credentials |
| **Service Mesh / DNS**| Kubernetes CoreDNS | Built-in | Internal service discovery across pods |

---

## 5. Project Directory Structure

```
Project_8_Microservices_Kubernetes/
├── Dockerfiles /
│   ├── frontend/Dockerfile
│   ├── services/product-service/Dockerfile
│   ├── services/user-service/Dockerfile
│   ├── services/order-service/Dockerfile
│   └── services/notification-service/Dockerfile
│
├── frontend/
│   ├── package.json
│   ├── server.js                              # Express static file server & backend API proxy gateway
│   └── public/
│       ├── index.html                         # ShopSphere Dashboard interface
│       ├── style.css                          # Modern glassmorphic dark theme stylesheet
│       └── app.js                             # Client-side API polling & interactive order handler
│
├── services/
│   ├── product-service/
│   │   ├── package.json
│   │   └── server.js                          # Product catalog REST API with health probe
│   ├── user-service/
│   │   ├── package.json
│   │   └── server.js                          # User directory REST API with health probe
│   ├── order-service/
│   │   ├── package.json
│   │   └── server.js                          # Transactional order engine with inter-service RPC
│   └── notification-service/
│       ├── package.json
│       └── server.js                          # Event dispatch and logging service
│
├── k8s/
│   ├── namespace.yaml                         # Dedicated microservices-demo namespace
│   ├── configmap.yaml                         # Global environment configuration
│   ├── secret.yaml                            # Database credentials and API secret
│   ├── product-deployment.yaml                # Product service replica deployment
│   ├── product-service.yaml                   # Product ClusterIP service (Port: 3000)
│   ├── user-deployment.yaml                   # User service replica deployment
│   ├── user-service.yaml                      # User ClusterIP service (Port: 3000)
│   ├── order-deployment.yaml                  # Order service replica deployment
│   ├── order-service.yaml                     # Order ClusterIP service (Port: 3000)
│   ├── notification-deployment.yaml           # Notification service replica deployment
│   ├── notification-service.yaml              # Notification ClusterIP service (Port: 3000)
│   ├── frontend-deployment.yaml               # Frontend replica deployment
│   └── frontend-service.yaml                  # Frontend NodePort service (Port: 8080, NodePort: 30080)
│
├── screenshots/
│   ├── SCREENSHOTS_REQUIRED.md                # Verification checklist and evidence summary
│   ├── P8_01_kubernetes_deployments.png
│   ├── P8_02_services_configmap_secret.png
│   ├── P8_03_microservices_api_verification.png
│   └── P8_04_application_ui.png
│
└── README.md                                  # Comprehensive project documentation
```

---

## 6. Microservices Implementation Details

### 6.1. Product Service (`services/product-service/`)
- **Port:** 3000
- **Key Endpoints:**
  - `GET /health`: Returns the service status (`UP`), pod hostname (`os.hostname()`), uptime duration, and current environment.
  - `GET /api/products`: Responds with an array of 5 catalog entries containing IDs, prices, categories, stock levels, and ratings.
  - `GET /api/products/:id`: Retrieves a specific product by its identifier.

### 6.2. User Service (`services/user-service/`)
- **Port:** 3000
- **Key Endpoints:**
  - `GET /health`: Health check probe and telemetry data.
  - `GET /api/users`: Returns a list of registered user profiles (Lead Architect, DevOps Engineer, Product Manager, Security Specialist).
  - `GET /api/users/:id`: Retrieves a specific user by their identifier.

### 6.3. Order Service (`services/order-service/`)
- **Port:** 3000
- **Key Endpoints:**
  - `GET /health`: Reports health status, secret configuration verification (`API_SECRET_SET`), and the database username.
  - `GET /api/orders`: Returns a listing of existing transaction records.
  - `POST /api/orders`: Accepts an order payload (`userId`, `productId`, `quantity`). Carries out inter-service HTTP requests to validate the user through `USER_SERVICE_URL`, retrieve product details from `PRODUCT_SERVICE_URL`, and asynchronously dispatch a notification event to `NOTIFICATION_SERVICE_URL`.

### 6.4. Notification Service (`services/notification-service/`)
- **Port:** 3000
- **Key Endpoints:**
  - `GET /health`: Health check probe and event count metrics.
  - `GET /api/notifications`: Returns a time-ordered stream of dispatched system alerts and order notifications.
  - `POST /api/notifications`: Receives and broadcasts new alert and order confirmation events.

### 6.5. ShopSphere Web Frontend (`frontend/`)
- **Port:** 8080 (Container) / 30080 (NodePort)
- **Key Features:**
  - Concurrently aggregates health status from all 4 backend microservices via `GET /api/system/health`.
  - Renders real-time status indicators (`ONLINE` / `OFFLINE`), response latency measurements, and pod hostnames.
  - Provides an interactive "Place Order" modal that triggers full multi-service transaction workflows.

---

## 7. Docker Containerization

Every microservice is packaged using a multi-layered, Alpine-based Node.js Docker image optimized for minimal footprint and rapid startup.

Example Dockerfile (`services/product-service/Dockerfile`):
```dockerfile
FROM node:18-alpine

WORKDIR /usr/src/app

COPY package*.json ./
RUN npm install --omit=dev --no-audit

COPY . .

EXPOSE 3000

CMD ["node", "server.js"]
```

### Image Build Commands:
```bash
docker build -t shopsphere-frontend:latest ./frontend
docker build -t shopsphere-product-service:latest ./services/product-service
docker build -t shopsphere-user-service:latest ./services/user-service
docker build -t shopsphere-order-service:latest ./services/order-service
docker build -t shopsphere-notification-service:latest ./services/notification-service
```

---

## 8. Kubernetes Configuration

### 8.1. Namespace Isolation (`k8s/namespace.yaml`)
```yaml
apiVersion: v1
kind: Namespace
metadata:
  name: microservices-demo
  labels:
    app.kubernetes.io/name: microservices-demo
    environment: production
    managed-by: mohammad-ahmad-23070122140
```

### 8.2. Declarative Deployments (`k8s/*-deployment.yaml`)
Each Deployment specifies resource requests, limits, environment variable bindings sourced from ConfigMaps and Secrets, and automated health probe configurations.

Example Order Deployment (`k8s/order-deployment.yaml`):
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: order-service
  namespace: microservices-demo
  labels:
    app: order-service
    app.kubernetes.io/part-of: shopsphere
spec:
  replicas: 1
  selector:
    matchLabels:
      app: order-service
  template:
    metadata:
      labels:
        app: order-service
        app.kubernetes.io/part-of: shopsphere
    spec:
      containers:
        - name: order-service
          image: shopsphere-order-service:latest
          imagePullPolicy: IfNotPresent
          ports:
            - containerPort: 3000
              name: http
          envFrom:
            - configMapRef:
                name: shopsphere-config
            - secretRef:
                name: shopsphere-secret
          resources:
            requests:
              cpu: 50m
              memory: 64Mi
            limits:
              cpu: 200m
              memory: 128Mi
          livenessProbe:
            httpGet:
              path: /health
              port: 3000
            initialDelaySeconds: 5
            periodSeconds: 10
          readinessProbe:
            httpGet:
              path: /health
              port: 3000
            initialDelaySeconds: 3
            periodSeconds: 5
```

### 8.3. Kubernetes Services (`k8s/*-service.yaml`)
- **Backend Services:** Each exposes internal port 3000 through a `ClusterIP` type (`product-service`, `user-service`, `order-service`, `notification-service`).
- **Frontend Service:** Exposes port 8080 to external traffic via a `NodePort` type (nodePort: `30080`).

---

## 9. ConfigMap and Secret Management

### 9.1. Environment ConfigMap (`k8s/configmap.yaml`)
Supplies centralized, non-sensitive service URLs and port mappings that all pods consume through `envFrom`:
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: shopsphere-config
  namespace: microservices-demo
data:
  APP_ENV: "production"
  SERVICE_PORT: "3000"
  FRONTEND_PORT: "8080"
  PRODUCT_SERVICE_URL: "http://product-service:3000"
  USER_SERVICE_URL: "http://user-service:3000"
  ORDER_SERVICE_URL: "http://order-service:3000"
  NOTIFICATION_SERVICE_URL: "http://notification-service:3000"
```

### 9.2. Sensitive Credentials Secret (`k8s/secret.yaml`)
Delivers sensitive credentials that are injected into backend microservice pods:
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: shopsphere-secret
  namespace: microservices-demo
type: Opaque
stringData:
  DB_USERNAME: "shopsphere_admin"
  DB_PASSWORD: "K8sSecureOrderPassword2026!"
  API_SECRET: "jwt-mesh-secret-token-key-23070122140"
```

---

## 10. Deployment and Verification Guide

### 10.1. Step 1: Create Namespace and Apply Configurations
```bash
kubectl apply -f k8s/namespace.yaml
kubectl apply -f k8s/configmap.yaml
kubectl apply -f k8s/secret.yaml
```

### 10.2. Step 2: Deploy All Microservices and Frontend
```bash
kubectl apply -f k8s/
```

### 10.3. Step 3: Verify Resource Health
```bash
# Inspect all deployments and pods within the namespace
kubectl get deployments,pods -n microservices-demo -o wide

# Inspect services, configmaps, and secrets
kubectl get svc,configmap,secret -n microservices-demo
```

### 10.4. Step 4: Verify API Endpoints & Inter-Service RPC
```bash
# Port-forward the frontend service
kubectl port-forward svc/frontend-service 8080:8080 -n microservices-demo

# In a separate terminal:
curl -s http://localhost:8080/health
curl -s http://localhost:8080/api/system/health
curl -s http://localhost:8080/api/products
curl -s http://localhost:8080/api/users
curl -s http://localhost:8080/api/orders
curl -s http://localhost:8080/api/notifications
```

---

## 11. Web UI Demonstration (ShopSphere Dashboard)

Navigating to `http://localhost:8080` opens the **ShopSphere Microservices Dashboard**:
1. **Mesh Telemetry Matrix:** Live health status cards showing active pod identifiers and response latency readings for the Product, User, Order, and Notification services.
2. **Product Catalog Grid:** An interactive catalog view presenting items, pricing, stock availability, and quick-order actions.
3. **Users Directory:** A listing of customer and administrator profiles.
4. **Orders Queue:** A real-time table displaying placed transactions.
5. **Interactive Order Dispatch:** Submitting an order dynamically calls the Order Service, which queries the Product and User services through Kubernetes DNS, persists the record, and fires an event to the Notification Service.

---

## 12. Verified Execution Screenshots

The screenshots below confirm successful live execution on the Kubernetes cluster:

### Screenshot 1: Kubernetes Deployments and Pod Readiness
![Kubernetes Deployments and Pods](./screenshots/P8_01_kubernetes_deployments.png)
*Figure 12.1: Terminal output confirming all 5 deployments and pods are running with 1/1 Ready status within the `microservices-demo` namespace.*

### Screenshot 2: Services, ConfigMap, and Secret Verification
![Services, ConfigMaps, and Secrets](./screenshots/P8_02_services_configmap_secret.png)
*Figure 12.2: Terminal output validating ClusterIP and NodePort services, ConfigMap environment values, and Secret injection.*

### Screenshot 3: Microservices API Verification & Inter-Service Communication
![Microservices API Verification](./screenshots/P8_03_microservices_api_verification.png)
*Figure 12.3: Verification of `/health` and REST endpoints showcasing DNS-based service discovery and RPC communication.*

### Screenshot 4: ShopSphere Web UI Dashboard
![ShopSphere Web UI](./screenshots/P8_04_application_ui.png)
*Figure 12.4: Live browser view of the ShopSphere Dashboard running on Kubernetes, displaying healthy service telemetry, the product catalog, and active orders.*

---

## 13. Conclusion

**Project 8** successfully demonstrates a production-ready multi-tier microservices application orchestrated on Kubernetes:
1. **Modularity & Decoupling:** Four independent Node.js Express backend microservices and one web frontend tier, each operating in isolation.
2. **Kubernetes Core Primitives:** Full utilization of Deployments, ClusterIP/NodePort Services, ConfigMaps, and Secrets.
3. **Service Discovery:** Dependable internal communication through Kubernetes DNS service names, with no hardcoded host addresses.
4. **Zero Downtime & Self-Healing:** Automated health verification via liveness and readiness probes ensuring continuous cluster resilience.
5. **Live Verification:** Confirmed through automated CLI testing and interactive web UI demonstration.
