from flask import Flask,redirect,render_template,request

app=Flask(__name__)



@app.route("/user")
def normal_user():
    return "welcome user"

@app.route("/guest")
def guest():
    return "welcome guest"

@app.route("/register")
def registration():
    return render_template("registration.html")



@app.route("/confirmation",methods=["POST","GET"])
def display_data():
    if request.method == 'POST':
        data=request.form
        return render_template("confirmation.html",reg_details=data)
        

@app.route("/users/<name>")
def users(name):
    if name=="user":
        return redirect("/user")
    if name=="guest":
        return redirect("/guest")
if(__name__=="__main__"):
    app.run(debug=True)    