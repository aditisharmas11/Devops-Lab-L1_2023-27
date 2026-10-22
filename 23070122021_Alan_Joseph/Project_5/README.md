# Project 5 - Containerizing a Spring Boot App and Scanning the Image with Trivy

A Spring Boot REST API for a retail company, packaged with a multi-stage Dockerfile and scanned for vulnerabilities with Trivy.

## Endpoints
- `GET /` - welcome message
- `GET /api/products` - list products
- `GET /api/products/{id}` - one product

## Build, run, scan
```bash
scripts/build-image.sh            # builds retail-app:1.0
scripts/run.sh                    # runs it on http://localhost:8080
curl http://localhost:8080/api/products
scripts/scan-with-trivy.sh        # scans the image for HIGH and CRITICAL CVEs
```

Or with Compose:
```bash
docker compose up --build
```

## Notes
- The Dockerfile builds the jar in a Maven stage and copies only the jar into a slim JRE image.
- `scan-with-trivy.sh` runs Trivy as a container, so no local install is needed.
