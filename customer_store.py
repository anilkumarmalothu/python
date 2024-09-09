import pymongo


from pymongo import MongoClient
try:
    myclient=MongoClient("mongodb+srv://anilmalothu:anil1234@cluster0.dqicphj.mongodb.net/")
    mydb=myclient["database"]
    mycol=mydb["emp_datas"]


    def insertdata(mydata):
        try: 
            mycol.insert_one(mydata)
            print("data is successfully inserted")
        except Exception as e:
            print(e)
    def updatedata(mydata,newdata):
        try:
            x=mycol.find_one(mydata)
            if x is not None: 
                mycol.update_one(mydata,{"$set":newdata})
                print("data is updated successfully")
            else:
                print(f"the type {mydata} is not exist: ")
                return    
        except Exception as e:
            print(e)
    def deletedata(deldata):
        try:
            mycol.delete_one(deldata)
            print("data is successfully deleted")
        except Exception as e:
            print(e)
    print("1:insert\n 2:update\n 3:delete\n")
    c=int(input("choose the option"))
    match c:
        case 1:
            name=input("enter the name:")
            address=input("enter the address")
            mydta={
                "name":name,
                "address":address
            }
            insertdata(mydta)
        case 2:
            name=input("enter the name of document which need update:")
            mydata={"name":name}
            name=input("enter the name which need to modify")
            address=input("enter new address")
            newdata={
                "name":name,
                "address":address
            }
            updatedata(mydata,newdata)
        case 3:
            name=input("enter the name of collection to delete :")
            dicti={"name":name}
            deletedata(dicti)  
        case __:
            print("incorrect option")
except Exception as e:
    print(e)