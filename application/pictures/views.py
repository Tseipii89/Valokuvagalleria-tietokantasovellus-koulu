from application import app, db
from flask import render_template, request
from application.pictures.models import Picture

@app.route("/pictures/new/")
def pictures_form():
    return render_template("pictures/new.html")

@app.route("/pictures/", methods=["POST"])
def pictures_create():
    vastaus = Picture(request.form.get("path"))

    db.session().add(vastaus)
    db.session().commit()

    return "onnistui"