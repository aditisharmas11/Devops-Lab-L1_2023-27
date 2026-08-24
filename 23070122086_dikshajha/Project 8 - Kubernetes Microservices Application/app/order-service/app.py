from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "service": "Order Service",
        "status": "running",
        "message": "Order service is working"
    })

@app.route("/orders")
def orders():
    return jsonify({
        "orders": [
            {"id": 101, "product": "Laptop", "quantity": 1},
            {"id": 102, "product": "Keyboard", "quantity": 2}
        ]
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
