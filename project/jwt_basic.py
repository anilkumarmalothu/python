from flask import *
from flask_jwt_extended import *


app=Flask(__name__)

app.config["JWT_SECRET_KEY"]="anil"
app.config["JWT_TOKEN_LOCATION"]=["headers"]

jwt=JWTManager(app)


@app.route("/login",methods=["POST"])
def login():
    username=request.json.get("username",None)
    passs=request.json.get("password",None)
    access_token=create_access_token(identity={username:username})
    if(username=="anil" and passs=="chennai"):
        return {"token" :access_token}
    return {"login":"failed"}
@app.route("/shop",methods=["GET"])
@jwt_required()
def shop():
    token=request.headers.get("Authorization")
    if(token):
        return {"shopping":"you can start your shopping successfully"}
    return {"shopping":"authentication issue"}
    
app.run()