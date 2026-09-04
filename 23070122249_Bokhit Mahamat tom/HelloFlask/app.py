from flask import Flask

app = Flask(__name__)
print("Main branch initializing application... User authentication module loading...")

@app.route("/")
def home():
    return "Hello World from Flask!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
