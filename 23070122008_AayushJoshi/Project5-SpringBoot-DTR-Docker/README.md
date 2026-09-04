# Project 5 — Containerizing Spring Boot App & Docker Image Scanning with DTR

**Student:** Aayush Joshi | **PRN:** 23070122008

---

## Overview

This project deploys a **Spring Boot retail application** for a company with multiple web services on Docker, and scans the Docker image using **Trivy** (simulating Docker Trusted Registry — DTR) for vulnerabilities before pushing to a registry.

---

## Architecture

```
Spring Boot Source (RetailHub)
        │
        ▼
Multi-Stage Docker Build
  ├── Stage 1: maven:3.9.6  →  mvn package (JAR)
  └── Stage 2: eclipse-temurin:17-jre-alpine  →  Run app

        │
        ▼
Trivy Image Scan (DTR Security Gate)
        │
        ▼
Docker Compose — Multiple Web Apps
  ├── retailhub-app   (Spring Boot @ :8080)
  └── nginx-gateway   (Nginx reverse proxy @ :80)
```

---

## Application — RetailHub REST API

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/products` | GET | List all products |
| `/api/products/{id}` | GET | Get product by ID |
| `/api/products` | POST | Add new product |
| `/api/products/category/{cat}` | GET | Filter by category |
| `/api/orders` | GET | List all orders |
| `/api/orders` | POST | Place a new order |
| `/api/orders/{id}/status` | PATCH | Update order status |
| `/actuator/health` | GET | Health check |

---

## Files

| File | Purpose |
|------|---------|
| `pom.xml` | Maven dependencies (Spring Web, Actuator) |
| `Dockerfile` | Multi-stage build: Maven → JRE Alpine |
| `docker-compose.yml` | Orchestrates Spring Boot + Nginx gateway |
| `nginx.conf` | Nginx reverse proxy routing to API |
| `Jenkinsfile` | CI/CD pipeline with Trivy DTR scan stage |
| `src/` | Spring Boot source — models + controllers |

---

## How to Run

```bash
# Build and start all services
docker compose up --build -d

# Verify containers
docker ps

# Test API
curl http://localhost:8080/api/products
curl http://localhost/api/products

# Health check
curl http://localhost:8080/actuator/health
```

---

## Docker Image Scan (DTR)

Trivy scans the image for HIGH/CRITICAL CVEs before deployment:

```bash
docker build -t retailhub:1.0.0 .

docker run --rm \
  -v /var/run/docker.sock:/var/run/docker.sock \
  aquasec/trivy:latest image \
  --severity HIGH,CRITICAL \
  retailhub:1.0.0
```

---

## Jenkins Pipeline Stages

| Stage | Description |
|-------|-------------|
| Checkout | Pull source from GitHub |
| Build JAR | `mvn clean package` |
| Build Docker Image | Multi-stage Docker build + tag for DTR |
| Scan Image with Trivy | Security scan (HIGH/CRITICAL vulnerabilities) |
| Push to DTR | Push scanned image to Docker Trusted Registry |
| Deploy | `docker compose up -d` — launch all services |

---

## Screenshots

![Spring Boot source structure](./screenshots/01-springboot-source.png)
![Docker build multi-stage output](./screenshots/02-docker-build.png)
![Docker compose up — both services running](./screenshots/03-docker-compose-up.png)
![API response at localhost:8080](./screenshots/04-api-response.png)
![Trivy DTR image scan results](./screenshots/05-trivy-scan.png)
![Jenkins pipeline all stages green](./screenshots/06-jenkins-pipeline.png)
