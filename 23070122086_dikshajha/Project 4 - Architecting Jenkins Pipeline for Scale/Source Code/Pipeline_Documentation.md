# Pipeline Documentation

## Project Title

**Architecting Jenkins Pipeline for Scale**

---

## Objective

The objective of this project is to configure a distributed Jenkins Pipeline that compiles and tests a Maven project using two different Jenkins agents (nodes). This demonstrates workload distribution and scalable CI/CD execution.

---

## Tools & Technologies Used

- Jenkins
- Maven
- Java 17
- JUnit 4
- Windows 11
- VS Code

---

## Project Architecture

The Jenkins setup consists of:

- Jenkins Controller (Built-In Node)
- Compile Agent (`compile-node`)
- Test Agent (`test-node`)

The controller manages the pipeline execution, while the agents perform the assigned tasks.

---

## Pipeline Workflow

### Stage 1: Compile

- Executed on the **compile-node** agent.
- Jenkins switches execution to the compile agent.
- Maven command executed:

```bash
mvn clean compile
```

- The source code is compiled successfully.

---

### Stage 2: Test

- Executed on the **test-node** agent.
- Jenkins switches execution to the test agent.
- Maven command executed:

```bash
mvn test
```

- JUnit test cases are executed successfully.

---

## Jenkins Agents

### 1. compile-node

**Purpose**

- Compiles the Maven project.

**Label**

```
compile
```

---

### 2. test-node

**Purpose**

- Executes JUnit test cases.

**Label**

```
test
```

---

## Commands Used

### Compile

```bash
mvn clean compile
```

### Test

```bash
mvn test
```

---

## Pipeline Stages

1. Start Pipeline
2. Execute Compile Stage on **compile-node**
3. Execute Test Stage on **test-node**
4. Display Build Result
5. Finish Pipeline

---

## Build Result

The pipeline completed successfully.

- Compile Stage: **SUCCESS**
- Test Stage: **SUCCESS**
- Maven Build: **SUCCESS**
- JUnit Tests: **PASSED**
- Pipeline Status: **SUCCESS**

---

## Screenshots Included

The following screenshots are included with the project:

- Jenkins Nodes
- Pipeline Dashboard
- Pipeline Stages
- Distributed Pipeline Console Output
- Maven Compile Success
- Maven Test Success

---

## Conclusion

This project successfully demonstrates a distributed Jenkins Pipeline using multiple Jenkins agents. The compile process was executed on the **compile-node**, while the testing process was executed on the **test-node**. The Maven project compiled successfully, all JUnit tests passed, and the pipeline completed successfully, demonstrating scalable continuous integration using Jenkins.