from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    """Return a simple Hello World response."""
    print("Welcome to the homepage!")
    print("User accessed the home page (Auth feature pending)")
    return "<h1>Hello, World!</h1><p>Welcome to the DevOps Lab Flask Application.</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
