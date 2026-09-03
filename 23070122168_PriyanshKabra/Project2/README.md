# Project 2: Deploy Angular Application in Docker Container

## Objective

Deploy an Angular application in a Docker container using the Angular CLI and Docker Compose for development and production.

## Technologies Used

- Angular CLI 21.2.22
- Node.js 22.23.2
- npm 10.9.8
- Docker
- Docker Compose
- Nginx

## Project Structure

```text
Project2_Angular_Docker/
├── README.md
├── docker-compose.yml
├── docker-compose.prod.yml
├── screenshots/
│   ├── 01_angular_app_running.png
│   ├── 02_angular_docker_running.png
│   ├── 03_compose_development.png
│   └── 04_compose_production.png
└── angular-app/
    ├── Dockerfile
    ├── angular.json
    ├── package.json
    ├── package-lock.json
    └── src/
````

## Angular Application

The Angular application was created using the Angular CLI with routing and Server-Side Rendering (SSR) enabled.

The application source code is located inside the `angular-app/` directory.

## Docker

The application is containerized using a multi-stage Docker build.

### Build Stage

The build stage uses Node.js 22 Alpine to:

1. Install the project dependencies.
2. Copy the Angular application source code.
3. Build the Angular application.

### Runtime Stage

The runtime stage uses Nginx Alpine to:

1. Copy the generated Angular browser files.
2. Serve the application using Nginx.
3. Expose port 80 inside the container.

This separates the application build environment from the lightweight production runtime.

## Development Deployment

The development deployment is defined in:

```text
docker-compose.yml
```

Start the development deployment with:

```powershell
docker compose up -d --build
```

The development container is:

```text
angular-compose-dev
```

Port mapping:

```text
8081:80
```

The development deployment was successfully verified in the browser at:

```text
http://localhost:8081
```

## Production Deployment

The production deployment is defined in:

```text
docker-compose.prod.yml
```

Start the production deployment with:

```powershell
docker compose -f docker-compose.prod.yml up -d --build
```

The production container is:

```text
angular-compose-prod
```

Port mapping:

```text
8082:80
```

The production deployment was successfully verified in the browser at:

```text
http://localhost:8082
```

## Docker Compose Verification

The running containers can be checked using:

```powershell
docker compose ps
```

For the production configuration:

```powershell
docker compose -f docker-compose.prod.yml ps
```

The development and production containers were successfully created and started during testing.

## Browser Verification

The Dockerized Angular application was verified through both Compose configurations.

### Development

```text
http://localhost:8081
```

### Production

```text
http://localhost:8082
```

Both deployments successfully displayed the Angular application.

## Evidence

The `screenshots/` directory contains evidence from the completed implementation:

```text
screenshots/
├── 01_angular_app_running.png
├── 02_angular_docker_running.png
├── 03_compose_development.png
└── 04_compose_production.png
```

These screenshots document the Angular application, Docker deployment, development Compose deployment, and production Compose deployment.

## Git

The project was committed and pushed to the GitHub repository.

The final structural update was committed with:

```text
Commit: 8df9a5c
Message: Align Project 2 with Docker Compose development and production
```

The `main` branch was successfully pushed to the remote repository.

## Result

The Angular application has been successfully containerized and deployed using Docker and Docker Compose.

Both development and production Compose configurations were successfully built, started, and verified in the browser.