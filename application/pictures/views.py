from application import app, db
from flask import redirect, render_template, request, url_for, flash
from flask_login import login_required, current_user
from application.pictures.models import Picture
from application.pictures.forms import PictureForm

@app.route("/pictures", methods=["GET"])
def pictures_index():
    return render_template("pictures/list.html", pictures = Picture.query.all())

@app.route("/pictures/new/")
@login_required
def pictures_form():
    return render_template("pictures/new.html", form = PictureForm())

@app.route("/delete_pictures/<picture_id>/", methods=["POST"])
@login_required
def remove_picture(picture_id):
    pic = Picture.query.get_or_404(picture_id)
    if current_user.id == pic.account_id:
        db.session().delete(pic)
        db.session().commit()
    else:
        flash('Sinulla ei ole oikeutta poistaa tätä kuvaa')
    

    return redirect(url_for("pictures_index"))

@app.route("/pictures/", methods=["POST"])
@login_required
def pictures_create():
    form = PictureForm(request.form)
    # Tarkistetaan lomakkeen tietojen oikeamuotoisuus
    if not form.validate():
        return render_template("pictures/new.html", form = form)

    # Otetaan talteen formista saadut tiedot
    
    pic = Picture(form.path.data)
    pic.date_taken = form.date_taken.data
    pic.account_id = current_user.id

    db.session().add(pic)
    db.session().commit()

    return redirect(url_for("pictures_index"))

