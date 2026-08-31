from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    print("User authentication workflow initialized.")
    return (
        "<html><body style='font-family:Segoe UI,sans-serif;padding:48px;"
        "background:#07111f;color:#e2e8f0'>"
        "<p style='color:#93c5fd'>TW1.3 Docker</p>"
        "<h1>Hello World — Git conflict resolved on main</h1>"
        "<p>Flask app running inside Docker on port 5000</p>"
        "</body></html>"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
