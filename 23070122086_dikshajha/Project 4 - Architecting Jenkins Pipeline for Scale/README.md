# Project 4 - Architecting Jenkins Pipeline for Scale

## Objective

This project demonstrates how to configure a distributed Jenkins Pipeline using multiple Jenkins agents.

The Compile stage is executed on one agent while the Test stage is executed on another agent.

---

## Technologies Used

- Jenkins
- Maven
- Java
- JUnit
- Windows

---

## Folder Structure

```
Project 4 - Architecting Jenkins Pipeline for Scale
│
├── README.md
├── Screenshots
└── Source Code
```

---

## Workflow

1. Created two Jenkins agents.
2. Connected both agents to Jenkins Controller.
3. Created a Maven project.
4. Configured a Jenkins Pipeline.
5. Compile stage executed on compile-node.
6. Test stage executed on test-node.
7. Verified successful pipeline execution.

---

## Result

The distributed Jenkins Pipeline successfully compiled and tested the Maven project using two separate Jenkins agents.

---

## Screenshots Included

- Jenkins Nodes
- Pipeline Dashboard
- Pipeline Stages
- Console Output
- Maven Compile Success
- Maven Test Success