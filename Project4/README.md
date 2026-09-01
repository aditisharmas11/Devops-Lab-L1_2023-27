# Project 4: Architecting Jenkins Pipeline for Scale

This project demonstrates how to set up a distributed Jenkins pipeline that compiles a Maven project on one slave node and tests it on another.

## Overview

In Jenkins, when you distribute jobs across multiple slave nodes, the file systems are not shared. This means that if `Node 1` compiles the code and generates `.class` files in the `target/` directory, `Node 2` will not have those files when it tries to run the tests. 

To solve this, we use the Jenkins `stash` and `unstash` commands in our pipeline. `stash` saves a set of files from the current workspace so they can be transferred to another node, and `unstash` extracts them on the new node.

## Prerequisites

1. A Jenkins Controller (Master).
2. Two Jenkins Agent Nodes (Slaves) configured and connected to the Controller.
   - Node 1: Give it the label `node-1`. Must have Maven and JDK installed.
   - Node 2: Give it the label `node-2`. Must have Maven and JDK installed.
3. The Jenkins Git plugin and Pipeline plugin installed.

## Jenkins Setup Instructions

1. **Configure Nodes:**
   - Go to `Manage Jenkins` -> `Manage Nodes and Clouds` -> `New Node`.
   - Create two Permanent Agents.
   - Under the **Labels** field for the first node, add `node-1`.
   - Under the **Labels** field for the second node, add `node-2`.

2. **Create the Pipeline:**
   - Go to the Jenkins Dashboard -> `New Item`.
   - Enter a name (e.g., `Distributed-Maven-Pipeline`), select **Pipeline**, and click `OK`.
   - Under the **Pipeline** section, set **Definition** to `Pipeline script from SCM`.
   - Select `Git` as the SCM and provide the URL to this repository.
   - Ensure the **Script Path** is set to `Project4/Jenkinsfile` (since it is inside the Project4 folder).

3. **Run the Build:**
   - Click `Build Now`.
   - Check the console output. You should see:
     - The `Compile` stage executing on `node-1`.
     - The files being stashed.
     - The `Test` stage executing on `node-2`.
     - The files being unstashed and tests running successfully.

## Notes

- The provided `Jenkinsfile` uses the `bat` command for Windows-based Jenkins agents. If your agents are running Linux, replace `bat` with `sh` in the `Jenkinsfile`.
