#db.py 
from pymongo import MongoClient

config={
    "host":"localhost",
    "port":27017,
    "username":"",
    "password":""
}
class Myconnection:
    def __new__(cls,database):
        connection=MongoClient("mongodb+srv://anilmalothu:anil1234@cluster0.dqicphj.mongodb.net/")
        return connection[database]