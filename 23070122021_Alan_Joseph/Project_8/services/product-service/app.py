from flask import Flask, jsonify, abort

app = Flask(__name__)

PRODUCTS = [
    {"id": 1, "name": "Running Shoes", "price": 79.99},
    {"id": 2, "name": "Backpack", "price": 49.50},
    {"id": 3, "name": "Water Bottle", "price": 12.00},
]


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/products")
def list_products():
    return jsonify(PRODUCTS)


@app.route("/products/<int:product_id>")
def get_product(product_id):
    product = next((p for p in PRODUCTS if p["id"] == product_id), None)
    if product is None:
        abort(404, description="Product not found")
    return jsonify(product)


@app.errorhandler(404)
def not_found(err):
    return jsonify(error=str(err.description)), 404
