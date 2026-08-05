# Pipeline Documentation

## Objective

The objective of this project is to automate the Docker image build process for a Flask application using a Jenkins Declarative Pipeline.

---

## Technologies Used

- Jenkins
- Docker
- Git & GitHub
- Flask (Python)
- Windows PowerShell

---

## Pipeline Workflow

### Stage 1: Checkout

The pipeline checks out the latest source code from the GitHub repository.

Repository:
https://github.com/jhadiksha65/HelloWorldFlask_TW1

---

### Stage 2: Build Docker Image

Jenkins executes the Docker build command to create a Docker image for the Flask application.

Command Used:

docker build -t helloworldflask_tw1-flask-app .

---

### Stage 3: Success

If the Docker image is built successfully, Jenkins displays a success message.

---

## Output

The Jenkins pipeline successfully checks out the source code and builds the Docker image.

The final build status is displayed in the Jenkins Console Output.