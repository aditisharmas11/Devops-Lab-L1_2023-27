from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return (
        "<html><body style='font-family:Segoe UI,sans-serif;padding:48px;"
        "background:#07111f;color:#e2e8f0'>"
        "<p style='color:#93c5fd'>Project 1</p>"
        "<h1>Jenkins CI/CD Pipeline Working</h1>"
        "<p>Flask app built and deployed by a Dockerized Jenkins pipeline.</p>"
        "</body></html>"
    )


@app.route("/health")
def health():
    return {"status": "ok", "service": "hello-world-flask"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
