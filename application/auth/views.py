from flask import render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user

from application import app, db
from application.auth.models import User
from application.auth.forms import LoginForm, RegisterForm

@app.route("/auth/login", methods = ["GET", "POST"])
def auth_login():
    if request.method == "GET":
        return render_template("auth/loginform.html", form = LoginForm())

    form = LoginForm(request.form)
    # mahdolliset validoinnit

    user = User.query.filter_by(username=form.username.data).first()
    if not user:
        return render_template("auth/loginform.html", form = form,
                               error = "Väärä käyttäjätunnus tai salasana")


    login_user(user)
    return redirect(url_for("index"))  

@app.route("/auth/logout")
def auth_logout():
    logout_user()
    return redirect(url_for("index")) 

@app.route("/auth/new/")
def register_form():
    return render_template("auth/new.html", form = RegisterForm())    


@app.route("/auth/", methods=["POST"])
def register_create():
    form = RegisterForm(request.form)

    # Otetaan talteen formista saadut tiedot
    
    newUser = User(username=form.username.data, password=form.password.data)
    user = User.query.filter_by(username=form.username.data).first()
    if not user:
        db.session().add(newUser)
        db.session().commit()
        return redirect(url_for("index"))
    else:
        flash('Käyttäjätunnus on jo käytössä')
        return redirect(url_for("index"))
    