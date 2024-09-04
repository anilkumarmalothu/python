from pymongo import MongoClient
try:

    myclient=MongoClient("mongodb+srv://anilmalothu:anil1234@cluster0.dqicphj.mongodb.net/")

    mydb=myclient["sample_amzetta"]

    mycol=mydb["sample"]
    collist=mydb.list_collection_names()

    if "sample" in collist:
        print("the collection exists")
        mydict={"name":"amzetta","address":"chennai"}
    mycol.update_one({"_id":"102"},{"$set":mydict})
    mycol.delete_one({"_id":"102"})
    print()

    doc=mycol.find()

    for d in doc:
        print(d)
except Exception as e:
    print(e)
finally:
    if myclient is not None:
        myclient.close()
        print("connection successfully closed") 
        print("thank you coder")   
    