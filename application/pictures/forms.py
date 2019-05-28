from flask_wtf import FlaskForm
from wtforms import StringField, validators
from wtforms.fields.html5 import DateField

class PictureForm(FlaskForm):
    path = StringField("Lisää kuvan url", [validators.URL(require_tld=True, message=None)])
    date_taken = DateField("Kuvan ottamispäivämäärä", format="%Y-%m-%d")
 
    class Meta:
        csrf = False