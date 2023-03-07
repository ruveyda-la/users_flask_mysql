from flask_app.models.user import User
from flask_app import app
from flask import render_template, request, redirect,session

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
    if not User.validate_user(request.form):
        session['first_name']= request.form['first_name']
        session['last_name']=request.form['last_name']
        session['email']=request.form['email']
        return redirect("/correct")

    User.save(request.form)
    print(request.form)
    return redirect("/")

@app.route("/correct")
def correct_user_form():
    return render_template("correct.html")


@app.route("/users/<int:id>/edit")
def edit(id):
    data={'id':id}
    user= User.get_one(data)
    return render_template('edit.html',user=user)

@app.route("/users/update", methods=['POST'])
def update():
    id=request.form['id']
    if not User.validate_user(request.form):
        return redirect(f"/users/{id}/edit")
    User.change(request.form)
    return redirect (f"/users/{id}")

@app.route("/users/<int:id>/delete")
def delete(id):
    data={'id':id}
    User.delete_user(data)
    return redirect("/")











            
