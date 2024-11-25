from functools import wraps
from flask import request, jsonify
from db import check_api_key, get_user_from_api_key

def require_api_key(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        api_key = request.headers.get("X-API-Key")
        if not api_key:
            return jsonify({"error": "Unauthorized: Missing API Key"}), 401
            
        if not check_api_key(api_key):
            return jsonify({"error": "Unauthorized: Invalid API Key"}), 401

        user = get_user_from_api_key(api_key)
        if not user:
            return jsonify({"error": "Unauthorized: Invalid user"}), 401
            
        return f(user, *args, **kwargs)
    return decorated_function
