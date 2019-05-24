from flask_wtf import FlaskForm
from wtforms import StringField 
from wtforms.fields.html5 import DateField

class PictureForm(FlaskForm):
    path = StringField("Lisää kuvan url")
    date_taken = DateField("Kuvan ottamispäivämäärä", format="%Y-%m-%d")
 
    class Meta:
        csrf = False