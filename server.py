from flask import Flask, render_template,request,redirect
# import the class from friend.py
from user import User
app = Flask(__name__)
@app.route("/")
def read():
    users = User.get_all()
    return render_template("read.html", users=users)

@app.route("/add")
def show_form():
    return render_template("create.html")

@app.route("/add/new",methods=['POST'])
def create():
    User.save(request.form)
    print(request.form)
    return redirect("/")







            
if __name__ == "__main__":
    app.run(debug=True)