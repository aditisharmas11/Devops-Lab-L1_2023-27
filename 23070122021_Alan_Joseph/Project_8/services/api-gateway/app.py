import os

import requests
from flask import Flask, Response, jsonify, request

app = Flask(__name__)

API_KEY = os.environ.get("GATEWAY_API_KEY", "")
ROUTES = {
    "users": os.environ["USER_SERVICE_URL"],
    "products": os.environ["PRODUCT_SERVICE_URL"],
    "orders": os.environ["ORDER_SERVICE_URL"],
}


@app.before_request
def check_api_key():
    if request.path == "/health":
        return None
    if API_KEY and request.headers.get("X-API-Key") != API_KEY:
        return jsonify(error="unauthorized"), 401
    return None


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/api/<service>", defaults={"path": ""}, methods=["GET", "POST"])
@app.route("/api/<service>/<path:path>", methods=["GET", "POST"])
def proxy(service, path):
    base = ROUTES.get(service)
    if base is None:
        return jsonify(error="unknown service"), 404
    url = f"{base}/{service}" + (f"/{path}" if path else "")
    resp = requests.request(request.method, url, json=request.get_json(silent=True), timeout=5)
    return Response(resp.content, status=resp.status_code,
                    content_type=resp.headers.get("Content-Type", "application/json"))
