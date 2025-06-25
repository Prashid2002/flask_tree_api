from flask import Blueprint, request, jsonify
from werkzeug.security import check_password_hash
from models.db import get_db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/login', methods=['POST'])
def login():
    db = get_db()
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = db.users.find_one({ "username": username })
    if user and check_password_hash(user["password"], password):
        return jsonify({ "success": True, "session_id": user.get("session_id") }), 200
    else:
        return jsonify({ "success": False, "message": "Invalid credentials" }), 401