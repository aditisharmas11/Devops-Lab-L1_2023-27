import math
import socket

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/")
def index():
    return jsonify(message="Hello from Project 6", pod=socket.gethostname())


@app.route("/cpu")
def cpu():
    # Deliberately CPU-heavy so the HPA has something to react to
    n = int(request.args.get("n", 200000))
    total = sum(math.sqrt(i) for i in range(n))
    return jsonify(pod=socket.gethostname(), result=round(total, 2))


@app.route("/healthz")
def healthz():
    return "ok", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
