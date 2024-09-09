from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, create_access_token, jwt_required
import requests

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "amzetta123"
app.config["JWT_TOKEN_LOCATION"] = ["headers"]

jwt = JWTManager(app)

@app.route("/")
def home():
    return "Welcome to Flask Auth Service"

@app.route("/login", methods=["POST"])
def login_screen():
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")
    if username == "anil" and password == "chennai":
        access_token = create_access_token(identity={"username": username})
        return jsonify(access_token=access_token), 200
    return jsonify({"message": "Invalid credentials"}), 401

@app.route("/admin/details", methods=["GET"])
@jwt_required()
def sample_details():
    token = request.headers.get("Authorization")
    if token:
        response = requests.get("http://localhost:5001/policies", headers={"Authorization": token})
        return jsonify({'message': "Welcome", 'data': response.json()}), 200
    return jsonify({'message': "No token"}), 401

if __name__ == "__main__":
    app.run(port=5000, debug=True)
