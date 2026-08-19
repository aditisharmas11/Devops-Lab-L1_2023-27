# Project 7: MongoDB and Mongo Express Deployment

## 1. Objective

The purpose of this experiment is to successfully deploy and manage a stateful database together with a web-based graphical interface inside a Kubernetes cluster. This setup keeps configuration values and sensitive credentials separate from the application pods, which aligns with standard containerization and Kubernetes best practices.

* **MongoDB:** A widely used NoSQL database deployed here to store data securely.
* **Mongo Express:** A web-based administrative interface that makes it easier to interact with MongoDB databases.
* **Kubernetes Resources:** The deployment uses standard Kubernetes objects such as Deployments for pod lifecycle management, Services for networking, Secrets for credential storage, and ConfigMaps for configuration data.

## 2. Architecture and Components

### Configuration and Security

To keep the applications secure and portable across environments, configuration is separated from the pod definitions.

* **Secret (`mongodb-secret`):** An Opaque Kubernetes Secret is used to store the root database credentials securely. The values `mongo-root-username` and `mongo-root-password` are Base64 encoded in this file.
* **ConfigMap (`mongodb-configmap`):** A ConfigMap stores the `database_url`, which points to `mongodb-service`. This allows the Mongo Express frontend to route internal traffic to the database correctly.

### MongoDB Backend Deployment

The database instance is created using specific deployment and service mappings.

* **Deployment (`mongodb-deployment`):** Deploys a single replica using the standard `mongo` container image. The container listens on port `27017` and initializes the root user using the `MONGO_INITDB_ROOT_USERNAME` and `MONGO_INITDB_ROOT_PASSWORD` environment variables from the `mongodb-secret`.
* **Service (`mongodb-service`):** An internal ClusterIP service that exposes the MongoDB pod to the rest of the cluster on TCP port `27017`.

### Mongo Express Frontend Deployment

The administrative interface is deployed to connect to the database and present a user-facing UI.

* **Deployment (`mongo-express-deployment`):** Deploys a single replica using the `mongo-express` container image. The application listens on port `8081` and connects to the database by injecting `ME_CONFIG_MONGODB_ADMINUSERNAME` and `ME_CONFIG_MONGODB_ADMINPASSWORD` from the Secret. It also identifies the database server using `ME_CONFIG_MONGODB_SERVER` from the ConfigMap.
* **Service (`mongo-express-service`):** A NodePort service designed to expose the Mongo Express UI outside the Kubernetes cluster. It forwards external traffic from the node's port `30000` to the container's target port `8081` over TCP.

## 3. Implementation Steps

Based on the provided manifest files, the deployment followed these stages:

1. **Applied the Secret:** Ran `mongo-secret.yaml` to load the database root username and password into the cluster securely.
2. **Applied the ConfigMap:** Ran `mongo-configmap.yaml` to define the internal DNS name (`mongodb-service`) for the database.
3. **Deployed the Database:** Ran `mongo.yaml` to start the MongoDB pod and its internal networking service.
4. **Deployed the Frontend:** Ran `mongo-express.yaml` to launch the web GUI, connect it to the backend using the Secret and ConfigMap, and expose it externally on NodePort `30000`.

## 4. Verification and Results

To confirm the deployment was successful, the application was accessed through the exposed NodePort.


The deployment successfully demonstrates how MongoDB and Mongo Express can be integrated inside a Kubernetes cluster using Deployments, Services, Secrets, ConfigMaps, and NodePort networking.
