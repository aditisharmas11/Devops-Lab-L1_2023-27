# Project 2 — Deploy Angular Application in Docker

## Objective

Deploy an Angular application using **Docker** and **Docker Compose** for development and production environments.

## Technologies

* Angular
* Angular CLI
* Node.js 22
* Docker
* Docker Compose
* Nginx

## Project Structure

```text
Project_2_Angular_Docker/
├── angular-docker-app/
│   ├── Dockerfile.dev
│   ├── package.json
│   ├── package-lock.json
│   └── src/
├── Dockerfile
├── docker-compose.yml
├── docker-compose.prod.yml
├── .dockerignore
├── screenshots/
└── README.md
```

## Run Development

```bash
docker compose up --build
```

Access: `http://localhost:4200`

## Run Production

```bash
docker compose -f docker-compose.prod.yml up --build
```

Access: `http://localhost:8080`
