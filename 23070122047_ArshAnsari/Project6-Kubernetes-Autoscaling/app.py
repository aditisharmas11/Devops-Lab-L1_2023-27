from flask import Flask
import hashlib
import os
import time

app = Flask(__name__)


@app.get("/")
def home():
    return {
        "service": "social-feed",
        "prn": "23070122047",
        "message": "Social media feed API",
    }


@app.get("/feed")
def feed():
    # Burn CPU so HPA can observe utilization and scale replicas.
    deadline = time.time() + float(os.getenv("FEED_WORK_SECONDS", "0.35"))
    nonce = os.urandom(16)
    digest = nonce
    while time.time() < deadline:
        digest = hashlib.sha256(digest).digest()
    return {
        "items": [
            {"id": 1, "author": "arsh", "text": "Shipped a Kubernetes HPA demo"},
            {"id": 2, "author": "lab", "text": "Autoscale under load"},
        ],
        "hash": digest.hex(),
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
