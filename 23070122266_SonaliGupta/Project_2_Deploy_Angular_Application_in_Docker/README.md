# Project 2: Deploy Angular Application in Docker Container

### Objective
The objective of this project is to build an Angular application and package it inside a Docker container so that it can be built once and run consistently on any machine, supporting both development mode (via Angular CLI) and production mode served using Nginx via Docker Compose.

---

### Technologies Used

| Technology | Purpose |
| :--- | :--- |
| **Angular** | Frontend framework |
| **Angular CLI** | Project scaffolding, compilation, and development server |
| **Docker** | Containerization platform |
| **Docker Compose** | Multi-container orchestration (Dev & Prod services) |
| **Nginx** | High-performance web server for hosting production build |

---

### Screenshots

#### 1. Codebase & Docker Configuration
![Codebase Setup](Screenshots/01_codebase_setup.png)

#### 2. Development Environment Execution
![Dev Build Run](Screenshots/02_dev_server_run.png)

#### 3. Development Browser Output (localhost:4200)
![Dev Output](Screenshots/03_dev_browser_output.png)

#### 4. Production Container & Process Status (docker ps)
![Production Status](Screenshots/04_prod_container_run.png)

#### 5. Production Browser Output (localhost:8080)
![Production Output](Screenshots/05_prod_browser_output.png)
