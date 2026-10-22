# Project 2 - Deploy Angular Application in Docker Container

An Angular application built with the Angular CLI and containerised with Docker. Docker Compose provides a **development** setup (live reload) and a **production** setup (static build served by nginx).

## Production
```bash
docker compose up --build
```
Open http://localhost:8080

## Development
```bash
docker compose -f docker-compose.dev.yml up --build
```
Open http://localhost:4200

Stop either setup with Ctrl+C, or `docker compose down`.

## Files
- `Dockerfile` - multi-stage: development, build, production (nginx)
- `docker-compose.yml` / `docker-compose.dev.yml` - production and development services
- `nginx.conf` - SPA routing and a `/health` endpoint
