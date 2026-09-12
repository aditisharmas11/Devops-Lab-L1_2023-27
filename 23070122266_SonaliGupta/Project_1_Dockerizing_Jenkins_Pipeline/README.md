# Project 1: Dockerizing Jenkins Pipeline

**Name:** Sonali Gupta  
**PRN:** 23070122266  

---

### 1. Objective
To automate the build and deployment of a Python Flask web application using a declarative Jenkins CI/CD pipeline and Docker.

---

### 2. What Was Done
1. **App & Dockerfile:** Created a basic Flask app (`app.py`) running on port 5000 and wrote a `Dockerfile` using `python:3.9-slim`.
2. **Jenkinsfile:** Wrote a declarative pipeline script with 5 stages (`Checkout Code`, `Verify Environment`, `Build Docker Image`, `Run Container & Test`, and `Cleanup Environment`).
3. **Jenkins Setup:** Created a Pipeline job connected directly to GitHub via SCM to pull and run the `Jenkinsfile`.
4. **Execution:** Successfully ran the build in Jenkins and verified the container locally on `http://localhost:5000`.

---

### 3. Verification Screenshots

#### 1. Codebase & Dockerfile Setup
![Source Code and Dockerfile]![alt text](image-6.png)

#### 2. Jenkins Pipeline SCM Configuration
![Jenkins Pipeline Configuration]![alt text](image.png)![alt text](image-1.png)

#### 3. Jenkins Pipeline Stage View (Build Success)
![Pipeline Execution Stages]![alt text](image-2.png) 
![alt text](image-3.png)
#### 4. Running Docker Container
![Docker Container Running]![alt text](image-4.png)

#### 5. Web Browser Output (localhost:5000)
![App Browser Verification]![alt text](image-5.png)