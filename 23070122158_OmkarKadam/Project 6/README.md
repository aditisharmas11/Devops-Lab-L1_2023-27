# Project 6: Jenkins Docker Plugin Implementation

## Overview
This project demonstrates a Jenkins Pipeline that utilizes the Jenkins Docker pipeline plugin to:
1. Build a Java Maven project.
2. Build a Docker image containing the compiled artifact.
3. Push the resulting image to DockerHub.

## Prerequisites
- Jenkins with **Docker Pipeline Plugin** and **Docker plugin** installed.
- Docker installed on the Jenkins agent node.
- A DockerHub account.
- DockerHub credentials configured in Jenkins with the ID `dockerhub-credentials-id`.

## Project Structure
- `pom.xml`: Defines the Maven project and uses the `maven-shade-plugin` to package the app into a fat executable JAR.
- `src/`: Java source code for the application.
- `Dockerfile`: Multi-stage or simple Docker configuration to run the Java app.
- `Jenkinsfile`: Declarative Jenkins pipeline script to automate the CI/CD workflow.

## Jenkinsfile Breakdown
1. **Build Maven Project**: Executes `mvn clean package` to build the app and generate `target/portfolio-1.0-SNAPSHOT.jar`.
2. **Build Docker Image**: Uses `docker.build()` to create a Docker image from the `Dockerfile`.
3. **Push to DockerHub**: Uses `docker.withRegistry()` to authenticate with DockerHub and push the image.

## Setup Instructions
1. Replace `dockerhub-credentials-id` in the `Jenkinsfile` with your actual Jenkins Credentials ID.
2. Replace `yourdockerhubusername` with your DockerHub namespace.
3. Configure a Pipeline job in Jenkins pointing to this `Jenkinsfile`.
4. Trigger the build.
