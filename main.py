#main1.py
from flask import *
import requests
from flask_jwt_extended import *
from database import Myconnection 
from uuid import uuid1
from flask import request
from bson.json_util import dumps

app=Flask(__name__)
app.config["SECRET_KEY"]="amzetta"
app.config["JWT_TOKEN_LOCATION"]=["headers"]

jwt=JWTManager(app)

db=Myconnection('school_management')

@app.post('/user')
def insert_user(): #registration

    _id=str(uuid1().hex)
    details=dict(request.json)
    #details=dict(request.form)
    details.update({"_id":_id})
    result=db.user.insert_one(dict(details))
    if not result.inserted_id:
        return {"message":"Failed to insert"},500
    return {
        "message":"success",
        "data":{
            "id":result.inserted_id
        }
    },201

@app.route("/login",methods=["POST"])
def login():
    data=dict(request.json)
    username=data["username"]
    password=data["password"]
    userinfo=dict(db.log.find_one({"username":username}))
    access_token=create_access_token(identity={"username":username})
    print(userinfo)
    if userinfo["username"]==username and userinfo["password"]==password:
        return {"token":access_token},200
        
    return {"user":"invalid user"},401

@app.get("/users")
@jwt_required()
def get_users():
    get_jwt_identity({"Authorization":"headers"})
    data=db.users.find({})
    users=dumps(data)
    return  users

@app.get("/user/<user_name>/")
@jwt_required()
def get_user(user_name):
    data=str(user_name)
    user=db.users.find_one({"username":data})
    hello=dumps(user)
    if user:
     return hello
    return {"user":"not found"}
    
   

@app.delete("/user/<user_name>/")
@jwt_required()
def delete_user(user_name):
    query={"username":user_name}
    result=db.users.delete_one(query)
    if not result.deleted_count:
        return {"message":"Failed to delete"},500
    return {"message":"Deleted success"},200 

@app.put("/user/<user_id>/")
def update_user(user_id):
    query={"_id":user_id}
    details={"$set": dict(request.json)}
    result=db.user.update_one(query,details)
    if not result.matched_count:
        return {"message":"Failed to update. Record is not found"},404
    if not result.modified_count:
        return {"message":"No Changes applied"},500
    return {"message":"Update success"},200

if __name__=="__main__":
    app.run(port=5001,debug=True)