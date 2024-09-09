from flask import Flask,url_for

app=Flask(__name__)

@app.route("/home/<int:num>/<stting>")
def welcome(num,stting):
    return f"welcome to my website{num} and {stting}"
@app.route("/contactus")
def contactus():
    return "reach out to us @ +91613261172"
def details(name):
    return f"hello iam sorry access denied for these website {name}"

app.add_url_rule("/details/<name>","details",details)


@app.route("/generate_url/<name>")
def generate_url(name):
    # Using url_for to generate the URL for the 'details' endpoint
    url = url_for('details', name=name)
    return f"The URL for the details page is: {url}"

if __name__=="__main__":
    app.run()
    