# Project 5 – Spring Boot + Docker

## Overview
A Spring Boot retail web application containerized using Docker.

## Technologies
- Java 21
- Spring Boot 3.5.5
- Maven
- Docker
- Docker Scout

## Application
The application exposes port 8080 inside the container and returns:

Retail Web Application is running successfully!

## Maven Build

Build and test:

mvn clean test

Result:
- Tests run: 1
- Failures: 0
- Errors: 0
- Skipped: 0
- BUILD SUCCESS

Package the application:

mvn clean package -DskipTests

Generated artifact:

target/retail-app-1.0.0.jar

## Docker

Build the image:

docker build -t retail-app:1.0 .

Run the container:

docker run -d --name retail-app-container -p 8081:8080 retail-app:1.0

Host port 8081 maps to container port 8080 because Jenkins is already using host port 8080.

Application URL:

http://localhost:8081/

Expected response:

Retail Web Application is running successfully!

## Docker Scout

Image inspection:

docker scout quickview retail-app:1.0

Vulnerability scan:

docker scout cves retail-app:1.0

Scout reported vulnerabilities across multiple severity levels. Scout recommendations indicated newer major Java runtime base-image tags, but the Project 5 implementation remains on Java 21 to match the reference implementation.

## Evidence

The screenshots directory contains:

1. 01_springboot_docker_running.png
2. 02_docker_image.png