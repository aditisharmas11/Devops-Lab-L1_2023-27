# Project 4 - Distributed Jenkins Pipeline with Two Slave Nodes

A Jenkins master dispatches work to two agents (`slave1`, `slave2`). The Maven project is **compiled on slave1** and **tested on slave2**.

## Layout
- `docker-compose.yml` - Jenkins master + two SSH agents
- `jenkins/` - master image
- `agents/` - agent image with JDK 17 and Maven
- `Jenkinsfile` - declarative pipeline with one stage per agent
- `src/`, `pom.xml` - sample Maven project

## Setup
1. Create an SSH key for the agents:
   ```bash
   ssh-keygen -t ed25519 -f agent_key -N ""
   export AGENT_PUBKEY="$(cat agent_key.pub)"
   ```
2. Start the stack:
   ```bash
   docker compose up -d --build
   ```
3. In Jenkins (http://localhost:8080, initial password via `docker exec jenkins cat /var/jenkins_home/secrets/initialAdminPassword`):
   - Add a credential of type *SSH Username with private key* (username `jenkins`, paste `agent_key`).
   - **Manage Jenkins -> Nodes -> New Node**:
     - `slave1`, permanent agent, remote root `/home/jenkins/agent`, labels `slave1`, launch method *SSH* host `agent1`
     - `slave2`, permanent agent, remote root `/home/jenkins/agent`, labels `slave2`, launch method *SSH* host `agent2`
4. Create a Pipeline job using *Pipeline script from SCM* with script path `Project_4/Jenkinsfile`.
5. Build now. Console output shows the compile stage running on `slave1` and the test stage on `slave2`.

## Local checks
```bash
scripts/compile.sh
scripts/test.sh
```
