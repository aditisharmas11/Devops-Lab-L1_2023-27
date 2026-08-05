# Deployment Documentation

## Objective

Deploy an Angular application inside a Docker container using Docker.

---

## Prerequisites

- Node.js
- Angular CLI
- Docker Desktop
- Docker Compose

---

## Step 1: Install Angular CLI

```bash
npm install -g @angular/cli@18
```

---

## Step 2: Create Angular Project

```bash
ng new angular-docker-app
```

---

## Step 3: Run Angular Application

```bash
ng serve
```

Application URL:

```
http://localhost:4200
```

---

## Step 4: Create Dockerfile

Created a multi-stage Dockerfile to build the Angular application and serve it using Nginx.

---

## Step 5: Create docker-compose.yml

Configured Docker Compose for the Angular application.

---

## Step 6: Build Docker Image

```bash
docker build -t angular-docker-app .
```

---

## Step 7: Run Docker Container

```bash
docker run -d -p 4200:80 --name angular-container angular-docker-app
```

---

## Step 8: Verify Running Container

```bash
docker ps
```

---

## Step 9: Open Application

```
http://localhost:4200
```

---

## Result

Successfully deployed the Angular application inside a Docker container.