# Project 1 - Dockerizing Jenkins Pipeline

Demonstrates continuous integration and delivery by running Jenkins itself in Docker and using it to test, build and deliver a small Python app as a Docker image.

## Layout
- `jenkins/Dockerfile` - Jenkins LTS image with the Docker CLI and Python installed
- `docker-compose.yml` - runs Jenkins with the host Docker socket mounted
- `app/` - sample Python app, tests and its own Dockerfile
- `Jenkinsfile` - pipeline: Checkout -> Install -> Test -> Build Image -> Deliver

## Steps
1. Start Jenkins:
   ```bash
   docker compose up -d --build
   ```
2. Get the initial admin password:
   ```bash
   docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword
   ```
3. Open http://localhost:8080, finish setup and install the suggested plugins.
4. Create a **Pipeline** job, choose *Pipeline script from SCM*, point it at this repo and set the script path to `Project_1/Jenkinsfile`.
5. Click **Build Now**. The Deliver stage prints `Hello, DevOps!` from the container.

## Stop
```bash
docker compose down
```
