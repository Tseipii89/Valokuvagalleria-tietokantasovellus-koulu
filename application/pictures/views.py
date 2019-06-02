from application import app, db
from flask import redirect, render_template, request, url_for, flash, session
from flask_login import login_required, current_user
from application.pictures.models import Picture
from application.pictures.forms import PictureForm
from application.likes.models import Like

@app.route("/pictures", methods=["GET"])
def pictures_index():
    return render_template("pictures/list.html", 
        currentUser = current_user,
        pictures = Picture.query.all(), 
        likes = Like.query.all(), 
        find_like=Like.find_users_with_like(),
        how_many=Like.how_many_likes()
    )

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

@app.route("/pictures/like/<picture_id>/", methods=["POST"])
@login_required
def likes_create(picture_id):
    


    pic = Picture.query.get_or_404(picture_id)

    if Like.query.filter(Like.account_id == current_user.id, Like.picture_id == pic.id).first() == None:
    
        like = Like(
        current_user.id,
            pic.id
        )

        db.session().add(like)
        db.session().commit()

        return redirect(url_for("pictures_index"))    
    else:
        flash('Et voi tykätä kuvasta uudestaan')    
        return redirect(url_for("pictures_index")) 

@app.route("/picture/like/delete/<picture_id>/", methods=["POST"])
@login_required
def likes_delete(picture_id):
    like = Like.query.get_or_404({
        "picture_id": picture_id, 
        "account_id": current_user.id
    })
    db.session().delete(like)
    db.session().commit()

    

    return redirect(url_for("pictures_index"))    
