# Project 5 - Containerizing Spring Boot Retail Application and Docker Image Scanning

## Objective

To containerize a Spring Boot retail application using Docker, perform Docker image security analysis using Docker Scout, and publish and retrieve the Docker image using Docker Hub.

## Technologies Used

* Java 21
* Spring Boot
* Maven
* Docker
* Docker Scout
* Docker Hub
* HTML/CSS
* Git/GitHub

## Project Structure

```text
Project5-SpringBoot-DTR/
│
├── README.md
├── Screenshots/
│   ├── Docker images.jpeg
│   ├── Docker Hub push.jpeg
│   ├── Docker Hub repository.jpeg
│   ├── Docker Hub tag 1.1.jpeg
│   ├── Docker Hub pull.jpeg
│   ├── Docker containers.jpeg
│   └── Retail Store application.jpeg
│
└── retail-app/
    ├── .mvn/
    ├── src/
    ├── .gitattributes
    ├── .gitignore
    ├── Dockerfile
    ├── HELP.md
    ├── mvnw
    ├── mvnw.cmd
    └── pom.xml
```

## 1. Spring Boot Application

The project is a Spring Boot retail application using the package:

```text
com.example.retail_app
```

The application contains:

* `RetailAppApplication.java`
* `RetailController.java`
* `application.properties`

The application was successfully built using Maven.

## 2. Maven Build

The Maven project is located inside:

```text
retail-app/
```

The Maven build was executed from this directory using:

```powershell
mvn clean package
```

The build completed successfully and generated:

```text
target/retail-app-0.0.1-SNAPSHOT.jar
```

The generated JAR was also checked to confirm that both the main application and controller classes were included.

## 3. Dockerfile

The Dockerfile uses the Eclipse Temurin Java 17 JRE image as the runtime environment.

The Docker image is created using:

```powershell
docker build -t retail-app .
```

## 4. Docker Image Build

The local Docker image was successfully created as:

```text
retail-app:latest
```

The image was approximately 497 MB in size.

## 5. Docker Container Execution

The initial application container was run using:

```powershell
docker run -d -p 8081:8080 --name retail-app-container retail-app
```

The application was successfully accessed through:

```text
http://localhost:8081
```

The browser displayed:

```text
Retail Application is running successfully in Docker!
```

## 6. Docker Hub Authentication

Docker Hub authentication was completed successfully using:

```powershell
docker login
```

The Docker Hub username used for this project is:

```text
dikas
```

## 7. Docker Hub Tagging

The local image was tagged for Docker Hub as:

```powershell
docker tag retail-app:latest dikas/retail-app:1.1
```

The resulting Docker Hub image reference is:

```text
dikas/retail-app:1.1
```

## 8. Docker Hub Push

The image was pushed to Docker Hub using:

```powershell
docker push dikas/retail-app:1.1
```

The push completed successfully.

Docker Hub repository:

```text
dikas/retail-app
```

The repository contains the required:

```text
1.1
```

tag.

## 9. Docker Hub Pull

The image was successfully retrieved from Docker Hub using:

```powershell
docker pull dikas/retail-app:1.1
```

The Docker Hub image was available locally after the pull.

## 10. Running the Docker Hub Image

The pulled Docker Hub image was run using:

```powershell
docker run -d -p 8081:8080 --name retail-app-container dikas/retail-app:1.1
```

The running container used:

```text
Image: dikas/retail-app:1.1
Host Port: 8081
Container Port: 8080
```

The application was then verified in the browser using:

```text
http://localhost:8081
```

The retail application displayed the successful Docker execution message.

## 11. Docker Scout Security Analysis

Docker Scout was installed and configured on the system.

An attempt was made to analyze the local image using:

```powershell
docker scout quickview retail-app:latest
```

Docker Scout successfully began indexing the image, but the analysis could not be completed because the Trivy Java vulnerability database could not be downloaded from:

```text
ghcr.io/aquasecurity/trivy-java-db:1
```

The process returned an `unexpected EOF` / TLS connection error while downloading the Java database.

A direct test also showed a TLS handshake timeout when attempting to access the same GHCR resource.

Docker Hub repository Scout image analysis was also unavailable because the current Docker Hub plan had reached its repository limit.

Therefore, no fabricated vulnerability results are reported in this project. The limitation was caused by the external security-database/network and account-plan restrictions, not by the Spring Boot application or Docker image.

## 12. Result

The following tasks were successfully completed:

* Spring Boot retail application created and built
* Maven build completed successfully
* Dockerfile created
* Docker image built successfully
* Docker container executed successfully
* Application verified through the browser
* Docker Hub authentication completed
* Image tagged as `dikas/retail-app:1.1`
* Image pushed to Docker Hub
* Docker Hub repository created
* Docker Hub tag `1.1` verified
* Docker Hub image pulled successfully
* Pulled Docker Hub image executed successfully
* Application verified again after running the Docker Hub image

## 13. Conclusion

The Spring Boot retail application was successfully containerized using Docker and published to Docker Hub. The image was tagged with version `1.1`, pushed to Docker Hub, pulled back, and successfully executed as a Docker container.

Docker Scout security analysis was attempted, but the Java vulnerability database could not be downloaded because of external GHCR connectivity problems, while Docker Hub Scout analysis was unavailable under the current repository-plan limit. All other required Docker and Docker Hub operations were successfully completed.
