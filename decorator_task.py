import datetime

def storetime(function):
    
    def innerfunction():
        obj=str(datetime.datetime.now())
        f1=open("time.txt","a+")
        f1.write(obj+"\n")
        f1.close()
        print("data saved")
        return function
    return innerfunction    


@storetime
def time_call():
    print("the time is stored")
time_call()    