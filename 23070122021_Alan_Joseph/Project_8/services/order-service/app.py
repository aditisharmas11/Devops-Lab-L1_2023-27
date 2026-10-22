import os

import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

USER_URL = os.environ["USER_SERVICE_URL"]
PRODUCT_URL = os.environ["PRODUCT_SERVICE_URL"]
orders = []


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/orders", methods=["GET"])
def list_orders():
    return jsonify(orders)


@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json(silent=True) or {}
    try:
        user_id = int(data["user_id"])
        product_id = int(data["product_id"])
        quantity = int(data.get("quantity", 1))
    except (KeyError, TypeError, ValueError):
        return jsonify(error="user_id, product_id and quantity must be integers"), 400

    user = requests.get(f"{USER_URL}/users/{user_id}", timeout=3)
    if user.status_code != 200:
        return jsonify(error="user not found"), 404

    product = requests.get(f"{PRODUCT_URL}/products/{product_id}", timeout=3)
    if product.status_code != 200:
        return jsonify(error="product not found"), 404

    p = product.json()
    order = {
        "id": len(orders) + 1,
        "user": user.json()["name"],
        "product": p["name"],
        "quantity": quantity,
        "total": round(p["price"] * quantity, 2),
    }
    orders.append(order)
    return jsonify(order), 201
