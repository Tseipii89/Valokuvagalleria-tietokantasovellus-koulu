from flask_wtf import FlaskForm
from wtforms import StringField, validators, Field
from wtforms.widgets import TextInput
from wtforms.fields.html5 import DateField

class HashtagListField(Field):
    widget = TextInput()

    def _value(self):
        if self.data:
            return u' '.join(self.data)
        else:
            return u''

    def process_formdata(self, valuelist):
        if valuelist:
            self.data = [x.strip() for x in valuelist[0].split(',')]
        else:
            self.data = [] 

class PictureForm(FlaskForm):
    path = StringField("Lisää kuvan url", [validators.URL(require_tld=True, message=None)])
    date_taken = DateField("Kuvan ottamispäivämäärä", format="%Y-%m-%d")
    hashtags = HashtagListField("Lisää hashtag")
 
    class Meta:
        csrf = False

       