from flask import Flask, jsonify
from flask_jwt_extended import JWTManager, jwt_required

app = Flask(__name__)

app.config["JWT_SECRET_KEY"] = "amzetta123"
app.config["JWT_TOKEN_LOCATION"] = ["headers"]

jwt = JWTManager(app)

@app.route("/")
def home():
    return "Welcome to Flask Policy Service"

@app.route("/policies")
@jwt_required()
def policies():
    return jsonify({"message": "Policy details"})

if __name__ == "__main__":
    app.run(debug=True, port=5001)
