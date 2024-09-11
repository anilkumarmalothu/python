from flask import *
from pymongo import *
import requests
from flask_jwt_extended import *
from uuid import *
from bson.json_util import dumps

app=Flask(__name__)
mydb=MongoClient("mongodb+srv://anilmalothu:anil1234@cluster0.dqicphj.mongodb.net/")
db=mydb["school_management"]
app.config["SECRET_KEY"]="anil"
app.config["JWT_TOKEN_LOCATION"]=["headers"]
jwt=JWTManager()
jwt.init_app(app)


@app.post("/register")
def register():
    data=dict(request.json)
    _id=str(uuid1().hex)
    data.update({"_id":_id})
    result=db.users.insert_one(dict(data))
    if not result.inserted_id:
        return {"id":"not inserted"}
    return {"id":"registeration successful","_id":result.inserted_id}


@app.post("/login")
def login():
    data=dict(request.json)
    user_id=data["_id"]
    password=data["password"]
    userinfo=db.users.find_one(dict(data))
    
    if(userinfo["_id"]==user_id and userinfo["password"]==password):
        access_token=create_access_token(identity={"data":data})
        return {"token":access_token}
    return {"user":"login failed","user":"register user"}


@app.get("/getuser")
@jwt_required()
def getuser():
    userdata=list(db.users.find({}))
   
        
    return jsonify(userdata)
  








@app.get("/getuser/<user_id>")
@jwt_required()
def getuser1(user_id):
    data=user_id
    userdata=db.users.find_one({"_id":data})
    if userdata:
        userinfo=dumps(userdata)
        return {"data":userinfo}
    return {"data":"user not found"}


@app.put("/updateuser/<user_id>")
@jwt_required()
def updateuser(user_id):
    query={"_id":user_id}
    data=dict(request.json)
    data_update={"$set":data}
    result=db.users.update_one(query,data_update)
    if not result.matched_count:
        return {"update":"failed"}
    if not result.modified_count:
        return {"update":"failed"}
    return {"update":"success"}


@app.delete("/delete/<user_id>")
@jwt_required()
def deleteuser(user_id):
    query={"_id":user_id}
    result=db.users.delete_one(query)
    if not result.deleted_count:
        return {"deletion":"failed"}
    return {"deletion":"success"}

app.run(debug=True,port=5002)

   
 