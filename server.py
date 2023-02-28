from flask import Flask, render_template,request,redirect

from user import User
app = Flask(__name__)
@app.route("/")
def read_all():
    users = User.get_all()
    return render_template("read_all.html", users=users)

@app.route("/users/<int:id>")
def read_one(id):
    data={'id':id}
    user= User.get_one(data)
    return render_template('read_one.html',user=user)

@app.route("/add")
def show_form():
    return render_template("create.html")

@app.route("/add/new",methods=['POST'])
def create():
    User.save(request.form)
    print(request.form)
    return redirect("/")


@app.route("/users/<int:id>/edit")
def edit(id):
    data={'id':id}
    user= User.get_one(data)
    return render_template('edit.html',user=user)

@app.route("/users/update", methods=['POST'])
def update():
    User.change(request.form)
    id=request.form['id']
    return redirect (f"/users/{id}")

@app.route("/users/<int:id>/delete")
def delete(id):
    data={'id':id}
    User.delete_user(data)
    return redirect("/")











            
if __name__ == "__main__":
    app.run(debug=True)