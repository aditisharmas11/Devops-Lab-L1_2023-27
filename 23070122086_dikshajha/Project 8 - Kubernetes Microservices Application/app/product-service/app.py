from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "Product Service",
        "status": "running",
        "message": "Product service is working"
    })

@app.route("/products")
def products():
    return jsonify({
        "products": [
            {"id": 1, "name": "Laptop", "price": 55000},
            {"id": 2, "name": "Keyboard", "price": 1500}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
