from flask import Flask, jsonify, request, redirect, url_for
from auth import require_api_key
from db import check_api_key, get_user_from_api_key

# Initialize Flask app
app = Flask(__name__)

# Root Route - Redirects to Public Route
@app.route("/")
def root():
    return redirect(url_for('public_route'))

# Public Route
@app.route("/public", methods=["GET"])
def public_route():
    return jsonify({"message": "This is a public route accessible without authentication."})

# Secure Route
@app.route("/secure", methods=["GET"])
@require_api_key
def secure_route(user):
    return jsonify({"message": f"Hello, {user['name']}. You have accessed a secure route."})

# Secure Sentiment Analysis
@app.route("/secure/get_sentimen_user", methods=["GET"])
@require_api_key
def get_sentimen_user(user):
    # Simulated sentiment analysis logic
    sentiment = "positive" if user["name"] == "Alice" else "neutral"
    return jsonify({
        "user": user["name"],
        "sentiment": sentiment,
        "message": "Sentiment analysis completed successfully."
    })

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8000, debug=True)