from flask import Flask

app=Flask(__name__)

@app.route("/home/<name>")
def welcome(name):
    return f"welcome to my website {name}"
@app.route("/contactus")
def contactus():
    return "reach out to us @ +91613261172"
def details(name):
    return f"hello iam sorry access denied for these website {name}"

app.add_url_rule("/details/<name>","details",details)
if __name__=="__main__":
    app.run(port=5001)
    