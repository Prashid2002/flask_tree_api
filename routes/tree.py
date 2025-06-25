from flask import Blueprint, jsonify
from models.db import get_db

tree_bp = Blueprint('tree', __name__)

@tree_bp.route('/tree/<session_id>', methods=['GET'])
def get_tree_data(session_id):
    db = get_db()
    tree = db.tree_data.find_one({ "session_id": session_id })
    if tree:
        return jsonify({ "tree_data": tree["tree"] }), 200
    else:
        return jsonify({ "message": "Tree not found" }), 404