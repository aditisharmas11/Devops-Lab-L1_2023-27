# Project 5 — Containerizing a Spring Boot retail app and scanning the image

**Student:** Arsh Ansari | **PRN:** 23070122047

Spring Boot 3 / Java 17 retail catalog API, multi-stage Docker image, then a **Trivy** vulnerability scan (DTR is not available on this lab machine; Trivy is the same class of image scan used with Docker Trusted Registry).

---

## App

| Endpoint | Purpose |
|----------|---------|
| `GET /` | Company + PRN |
| `GET /catalog` | Sample retail SKUs |
| `GET /health` | Liveness |

Host port **8091 → 8080**.

```powershell
cd 23070122047_ArshAnsari\Project5-Spring-Boot-Docker-Scan
docker compose up --build -d
curl http://localhost:8091/catalog
```

## Scan (Trivy HIGH/CRITICAL)

```powershell
docker run --rm -v /var/run/docker.sock:/var/run/docker.sock aquasec/trivy:latest image --severity HIGH,CRITICAL --pkg-types os --scanners vuln retail-store:1.0.0
```

OS packages on `eclipse-temurin:17-jre-alpine` were scanned. Result: **3 HIGH, 0 CRITICAL** (OpenSSL CVE-2026-14456). DTR was not available on this lab PC; Trivy is the image scanner used in the same way.

---

## Evidence

![API catalog response](./screenshots/01-catalog.txt)
![Trivy image scan](./screenshots/02-trivy-scan.txt)
