# Project 2 - Angular Application with Docker

**Name:** Nigel Francy  
**PRN:** 23070122148

---

## Objective
This project focuses on containerizing an Angular application by using multi-stage Docker builds and separate development and production setups, with Nginx used to serve the app.

## Prerequisites
- Node.js and npm
- Docker
- Angular CLI

## Technologies Used
- Angular 21
- Docker
- Nginx
- Docker Compose

## Project Structure
```text
my-angular-app/
├── src/                        # Angular application source files
├── Dockerfile                  # Production-ready multi-stage build
├── Dockerfile.dev              # Development environment build
├── docker-compose.yml          # Development environment configuration
├── docker-compose.prod.yml     # Production environment configuration
└── .dockerignore
```

## Setup and Usage

### Development Environment
Run the following command to build and start the app in development mode:
```bash
docker-compose up --build
```
Once the containers are running, open: `http://localhost:4200`

### Production Environment
Use the following command to start the production build:
```bash
docker-compose -f docker-compose.prod.yml up --build
```
After startup, visit: `http://localhost:8080`
