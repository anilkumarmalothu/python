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




@app.get("/getuser/details")
@jwt_required()
def getuser():
        token=request.headers.get("Authorization")
        response=requests.get("http://localhost:5002/getuser",headers={"Authorization":token})
        return jsonify(response.json())

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


@app.delete("/delete")
@jwt_required()
def deleteprod():
    prod_id=(request.json)
    p_id=prod_id["_id"]
    token=request.headers.get("Authorization")
    response=requests.delete("http://localhost:5001/delete",headers={"Authorization":token},json=p_id)
    return jsonify(response.json())
#products
@app.post("/insertproducts")
@jwt_required()
def register():
    data=dict(request.json)
    _id=str(uuid1().hex)
    data.update({"_id":_id})
    result=db.products.insert_one(dict(data))
    if not result.inserted_id:
        return {"id":"not inserted"}
    return {"id":"product inserted successful","_id":result.inserted_id}

@app.get("/getproducts/details")
@jwt_required()
def getproduct():
        token=request.headers.get("Authorization")
        response=requests.get("http://localhost:5003/getproducts",headers={"Authorization":token})
        return jsonify(response.json())


@app.put("/updateproducts")
@jwt_required()
def updateproduct():
        token=request.headers.get("Authorization")
       
        data=request.json
        response=requests.put("http://localhost:5003/updateproduct",headers={"Authorization":token},json=data)
        return jsonify(response.json())


app.run(debug=True,port=5001)

   
 