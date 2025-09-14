from flask import Flask, jsonify, request, render_template
import json
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# In-memory storage for demo purposes
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com"},
    {"id": 2, "name": "Bob", "email": "bob@example.com"}
]

# Home route
@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Flask Learning API",
        "endpoints": {
            "GET /": "This home page",
            "GET /input": "Get sample data",
            "POST /submit": "Submit data",
            "GET /users": "Get all users",
            "GET /users/<id>": "Get user by ID",
            "POST /users": "Create new user",
            "PUT /users/<id>": "Update user",
            "DELETE /users/<id>": "Delete user"
        }
    })

# Original endpoints (improved)
@app.route("/input", methods=["GET"])
def get_input():
    return jsonify({
        "value": 42,
        "items": [1, 2, 3],
        "timestamp": datetime.now().isoformat(),
        "message": "Sample input data"
    })

@app.route("/submit", methods=["POST"])
def submit():
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "No JSON data provided"}), 400
    
    print("Received submission:", data)
    return jsonify({
        "status": "success",
        "received_data": data,
        "timestamp": datetime.now().isoformat()
    }), 200

# CRUD operations for users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify({"users": users, "count": len(users)})

@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    
    if not data or "name" not in data or "email" not in data:
        return jsonify({"error": "Name and email are required"}), 400
    
    new_user = {
        "id": max([u["id"] for u in users]) + 1 if users else 1,
        "name": data["name"],
        "email": data["email"]
    }
    users.append(new_user)
    
    return jsonify({"message": "User created", "user": new_user}), 201

@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    data = request.get_json()
    if not data:
        return jsonify({"error": "No data provided"}), 400
    
    user.update({k: v for k, v in data.items() if k in ["name", "email"]})
    return jsonify({"message": "User updated", "user": user})

@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    global users
    user = next((u for u in users if u["id"] == user_id), None)
    if not user:
        return jsonify({"error": "User not found"}), 404
    
    users = [u for u in users if u["id"] != user_id]
    return jsonify({"message": "User deleted", "deleted_user": user})

# Error handlers
@app.errorhandler(404)
def not_found(error):
    return jsonify({"error": "Endpoint not found"}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

if __name__ == "__main__":
    print("Starting Flask server...")
    print("Available at: http://localhost:3000")
    app.run(debug=True, port=3000)
