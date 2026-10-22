# Project 9 - Apache2 Server in a Kubernetes Deployment

Builds an image with Apache2 and a custom page, runs it as a Deployment, and reaches it from the host machine through a Service (NodePort) and kubectl port-forward.

## Steps
```bash
scripts/deploy.sh          # builds the image, loads it into minikube, applies manifests
scripts/inspect.sh         # shows pods, services, and Apache version inside the pod
scripts/access.sh          # prints the NodePort URL
scripts/port-forward.sh    # forwards localhost:8088 -> service port 80
```
Then open http://localhost:8088 (port-forward) or the URL from `access.sh`.

## Commands used
| Task | Command |
|---|---|
| Create resources | `kubectl apply -k k8s/` |
| List pods | `kubectl get pods -n apache-demo` |
| Describe a pod | `kubectl describe pod <pod> -n apache-demo` |
| Run a command in the pod | `kubectl exec deploy/apache-deployment -n apache-demo -- apache2 -v` |
| Logs | `kubectl logs deploy/apache-deployment -n apache-demo` |
| Access from host | `kubectl port-forward svc/apache-service 8088:80 -n apache-demo` |

## Clean up
```bash
scripts/cleanup.sh
```
