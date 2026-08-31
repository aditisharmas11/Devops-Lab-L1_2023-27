# Project 9 — Apache2 in a Kubernetes Deployment

**Student:** Arsh Ansari | **PRN:** 23070122047

`httpd:2.4` Deployment (2 replicas) with HTML from a ConfigMap. Access from the **host** using Kubernetes commands:

| Command | What it proves |
|---------|----------------|
| `kubectl apply -f k8s.yaml` | Create Deployment + Service |
| `kubectl get pods,svc` | Two pods + NodePort **30083** |
| `curl http://localhost:30083` | Host → NodePort |
| `kubectl port-forward svc/apache2 18080:80` | Host → API proxy |
| `kubectl exec` + `kubectl run busybox -- wget` | In-cluster access |

```powershell
kubectl apply -f k8s.yaml
curl http://localhost:30083
kubectl port-forward svc/apache2 18080:80
# another terminal: curl http://localhost:18080
kubectl exec deploy/apache2 -- cat /usr/local/apache2/htdocs/index.html
kubectl run curl-test --rm -it --image=busybox:1.36 --restart=Never -- wget -qO- http://apache2
```

---

## Evidence

![Pods and Service](./screenshots/01-kubectl.txt)
![Host curl via NodePort](./screenshots/02-host-curl.txt)
![port-forward and exec](./screenshots/03-k8s-commands.txt)
