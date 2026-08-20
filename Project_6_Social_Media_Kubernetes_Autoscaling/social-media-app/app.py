from flask import Flask, jsonify
import os
import time

app = Flask(__name__)


@app.route("/")
def home():
    return jsonify({
        "application": "Social Media API",
        "status": "running",
        "message": "Kubernetes Autoscaling Demo"
    })


@app.route("/health")
def health():
    return jsonify({
        "status": "healthy"
    })


@app.route("/posts")
def posts():
    return jsonify([
        {
            "id": 1,
            "username": "user1",
            "content": "Hello Kubernetes!"
        },
        {
            "id": 2,
            "username": "user2",
            "content": "Learning Kubernetes autoscaling."
        },
        {
            "id": 3,
            "username": "user3",
            "content": "DevOps makes deployment easier."
        }
    ])


@app.route("/load")
def load():
    start = time.time()

    while time.time() - start < 3:
        for i in range(100000):
            _ = i * i * i

    return jsonify({
        "message": "CPU load generated"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)