from flask import Flask, jsonify, abort

app = Flask(__name__)

USERS = [
    {"id": 1, "name": "Asha", "email": "asha@example.com"},
    {"id": 2, "name": "Ravi", "email": "ravi@example.com"},
    {"id": 3, "name": "Meera", "email": "meera@example.com"},
]


@app.route("/health")
def health():
    return jsonify(status="ok")


@app.route("/users")
def list_users():
    return jsonify(USERS)


@app.route("/users/<int:user_id>")
def get_user(user_id):
    user = next((u for u in USERS if u["id"] == user_id), None)
    if user is None:
        abort(404, description="User not found")
    return jsonify(user)


@app.errorhandler(404)
def not_found(err):
    return jsonify(error=str(err.description)), 404
