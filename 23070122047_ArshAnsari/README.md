# DevOps Lab L1 Submission — Arsh Ansari

| Detail | Value |
|--------|-------|
| **Name** | Arsh Ansari |
| **PRN** | 23070122047 |
| **Batch** | 2023–2027 |
| **GitHub** | [arshansari2880-alt](https://github.com/arshansari2880-alt) |
| **Submission branch** | `23070122047_ArshAnsari` |
| **Flask workflow repo** | [hello-world-flask](https://github.com/arshansari2880-alt/hello-world-flask) |

Submit folder: `23070122047_ArshAnsari` (PRN + name, no spaces).

---

## Assignment index

### TW1 — Continuous Evaluation: Foundational DevOps Skills (10 Marks)

| Assignment | Topic | Marks | Status |
|-----------|-------|-------|--------|
| [TW1.1 – Git Workflow & Collaboration](./TW1.1-Git-Workflow/README.md) | Git init, `feature/user-auth`, merge conflict | 4 | Done |
| [TW1.2 – Jira Project & Issue Tracking](./TW1.2-Jira/README.md) | Jira Scrum project, issues, board | 3 | Done |
| [TW1.3 – Docker & Jenkins Freestyle](./TW1.3-Docker-Jenkins-Freestyle/README.md) | Flask Dockerfile + Jenkins freestyle `ls` | 3 | Done |

### Projects

| Project | Topic | Status |
|---------|-------|--------|
| [Project 1 – Dockerizing Jenkins Pipeline](./Project1-Dockerized-Jenkins-Pipeline/README.md) | Declarative pipeline builds and runs a Docker image | Done |
| [Project 2 – React App in Docker](./Project2-React-Docker/README.md) | Multi-stage Node build, Nginx on port 80 | Done |
| [Project 4 – Distributed Jenkins (Maven)](./Project4-Distributed-Jenkins-Maven/README.md) | Master + `slave-1` + `slave-2` Maven portfolio | Done |

---

## Branching model

All lab work is on **one GitHub branch**: `23070122047_ArshAnsari`.

```
23070122047_ArshAnsari
├── TW1.1-Git-Workflow/
├── TW1.2-Jira/
├── TW1.3-Docker-Jenkins-Freestyle/
├── Project1-Dockerized-Jenkins-Pipeline/
├── Project2-React-Docker/
└── Project4-Distributed-Jenkins-Maven/
```

TW1.1 also uses a dedicated remote so the Git tasks are visible as real commits:

```
hello-world-flask
├── main
└── feature/user-auth
```

`feature/user-auth` was merged into `main` after a manual conflict resolution.

---

## How to run the deployed pieces locally

Docker Desktop must be running.

```powershell
# Flask Hello World (port 5000)
cd 23070122047_ArshAnsari\TW1.3-Docker-Jenkins-Freestyle
docker build -t hello-world-flask:latest .
docker run --rm -p 5000:5000 hello-world-flask:latest

# React portfolio (host port 3080 -> container 80)
cd ..\Project2-React-Docker
docker compose up --build -d

# Jenkins master + two Maven slaves (port 8080)
cd ..\Project4-Distributed-Jenkins-Maven
docker compose up --build -d
```

Jenkins login after CasC starts: **admin / admin123** (lab only).

Class submission target: https://github.com/aditisharmas11/Devops-Lab-L1_2023-27/
