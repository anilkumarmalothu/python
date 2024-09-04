from pymongo import MongoClient

myclient=MongoClient("mongodb+srv://anilmalothu:anil1234@cluster0.dqicphj.mongodb.net/")

mydb=myclient["sample_amzetta"]

mycol=mydb["sample"]
collist=mydb.list_collection_names()

if "sample" in collist:
    print("the collection exists")

mydict={"_id":"112","name":"amzetta_technologies","address":"chennai"}    
mylist=[{"name":"anil","address":"kodad"},{"name":"sreeram","address":"chennai"}]
# x=mycol.insert_one(mydict)
x=mycol.insert_many(mylist)
print(x.inserted_ids)
print()

doc=mycol.find()

for d in doc:
    print(d)
