from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

USER_SERVICE_URL = os.getenv("USER_SERVICE_URL", "http://user-service:5000")
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://product-service:5000")
ORDER_SERVICE_URL = os.getenv("ORDER_SERVICE_URL", "http://order-service:5000")

@app.route("/")
def home():
    user_data = requests.get(f"{USER_SERVICE_URL}/users").json()
    product_data = requests.get(f"{PRODUCT_SERVICE_URL}/products").json()
    order_data = requests.get(f"{ORDER_SERVICE_URL}/orders").json()

    return render_template(
        "index.html",
        users=user_data["users"],
        products=product_data["products"],
        orders=order_data["orders"]
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
