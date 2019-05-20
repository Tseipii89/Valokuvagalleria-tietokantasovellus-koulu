from application import app, db
from flask import redirect, render_template, request, url_for
from application.pictures.models import Picture


@app.route("/pictures", methods=["GET"])
def pictures_index():
    return render_template("pictures/list.html", pictures = Picture.query.all())

@app.route("/pictures/new/")
def pictures_form():
    return render_template("pictures/new.html")

@app.route("/delete_pictures/<picture_id>/", methods=["POST"])
def remove_picture(picture_id):
    
    pic = Picture.query.get_or_404(picture_id)
    db.session().delete(pic)
    db.session().commit()

    return redirect(url_for("pictures_index"))

@app.route("/pictures/", methods=["POST"])
def pictures_create():
    vastaus = Picture(request.form.get("path"))

    db.session().add(vastaus)
    db.session().commit()

    return redirect(url_for("pictures_index"))