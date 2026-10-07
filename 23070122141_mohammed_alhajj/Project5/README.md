# Project 5: Containerizing Application and Scanning Docker Image

This project deploys a Spring Boot web application on Docker for a retail company and demonstrates how to scan the resulting Docker image for vulnerabilities.

## 1. The Application
The application is a simple Java Spring Boot web server designed for a retail company. It exposes a few endpoints:
- `http://localhost:8080/` - Welcome message
- `http://localhost:8080/products` - Retail products placeholder

## 2. Containerizing the Application
We use a **multi-stage Dockerfile** to build and run the application. 
- Stage 1 uses a `maven` image to compile the Java code into a `.jar` file.
- Stage 2 uses a lightweight `jre-alpine` image to run the `.jar` file, keeping our final image size very small and secure.

### How to Build and Run
Open your terminal in this `Project5` folder and run:

1. **Build the Docker Image:**
   ```bash
   docker build -t retail-web-app:v1 .
   ```

2. **Run the Docker Container:**
   ```bash
   docker run -d -p 8080:8080 --name retail-app retail-web-app:v1
   ```
3. Open your browser and navigate to `http://localhost:8080` to see it running!

## 3. Scanning the Docker Image (DTR / Docker Scout)
Historically, enterprise users used **Docker Trusted Registry (DTR)** to host and scan images for vulnerabilities. Today, Docker has integrated scanning directly into Docker Desktop via **Docker Scout**.

To scan the image we just built for vulnerabilities:

1. Ensure you are logged into Docker Desktop.
2. Run the following command in your terminal to scan the local image:
   ```bash
   docker scout cves retail-web-app:v1
   ```
3. Docker Scout will output a list of any vulnerabilities (CVEs) found in the base image (`eclipse-temurin:17-jre-alpine`) or the Java dependencies listed in our `pom.xml`.
4. Alternatively, you can view the vulnerability report directly inside the **Docker Desktop GUI** by going to the "Images" tab, finding `retail-web-app:v1`, and clicking "View Packages and Vulnerabilities".

## 4. Cleanup
To stop and remove the container:
```bash
docker stop retail-app
docker rm retail-app
```
