from flask import Flask
import os
import urllib.request

app = Flask(__name__)


def fetch(url):
    try:
        with urllib.request.urlopen(url, timeout=8) as resp:
            return resp.read().decode()
    except Exception as exc:
        return f'{{"error": "{exc}"}}'


@app.get("/")
def gateway():
    user = fetch(os.environ["USER_URL"] + "/")
    product = fetch(os.environ["PRODUCT_URL"] + "/")
    order = fetch(os.environ["ORDER_URL"] + "/")
    return {
        "gateway": "frontend-gateway",
        "prn": "23070122047",
        "api_key_present": bool(os.environ.get("API_KEY")),
        "user": user,
        "product": product,
        "order": order,
    }


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
