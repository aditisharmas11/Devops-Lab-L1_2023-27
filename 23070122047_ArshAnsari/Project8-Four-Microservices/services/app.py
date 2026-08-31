from flask import Flask
import os

app = Flask(__name__)
SERVICE = os.environ.get("SERVICE_NAME", "unknown")


@app.get("/")
def root():
    return {
        "service": SERVICE,
        "prn": "23070122047",
        "status": "ok",
        "api_key_present": bool(os.environ.get("API_KEY")),
    }


@app.get("/health")
def health():
    return {"status": "UP", "service": SERVICE}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
