# Project 4: Architecting Jenkins Pipeline for Scale

## Overview
This project sets up a distributed Jenkins CI/CD pipeline using a controller-agent (Master-Slave) architecture to scale automated builds and testing across dedicated slave nodes.

## Node Architecture
* **Controller (Master):** Manages scheduling, triggers, and UI dashboard.
* **Slave Node 1 (`maven-build-node`):** Assigned label `maven-compile`. Responsible for repository checkout and Maven source compilation.
* **Slave Node 2 (`maven-test-node`):** Assigned label `maven-test`. Responsible for retrieving the compiled artifact workspace and executing test suites.

