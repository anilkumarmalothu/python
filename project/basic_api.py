from flask import *
from flask_jwt_extended import *
import requests
from pymongo import *
from bson.json_util import dumps


app=Flask(__name__)
mydb=MongoClient("mongodb+srv://anilmalothu:anil1234@cluster0.dqicphj.mongodb.net/")
db=mydb["school_management"]
app.config["SECRET_KEY"]="anil"
app.config["JWT_TOKEN_LOCATION"]=["headers"]


jwt=JWTManager(app)
@app.route("/register",methods=["POST"])
def register():
    data=dict(request.json)
    username=data["username"]
    userinfo=dict(db.users.find({"username":username}))
    if not userinfo:
         db.users.insert_one(data)
         return {"user":"registered successfully"}
    else:
       return {"user ":"already exist"}
@app.route("/login",methods=["POST"])
def login():
    
        data=dict(request.json)
        name=data["name"]
        home=data["home"]
        access_token=create_access_token(identity={"name":name})
        userinfo=dict(db.users.find_one({"name":name}))
        uname = userinfo["name"]
        info = userinfo["home"]
        if uname==name  and info == home:
            return {"token":access_token},200
        return {"user":"user not found"},401
        
        
        
       
     
    
    
        
if __name__=="__main__":
    app.run(port=5001,debug=True)
        
    