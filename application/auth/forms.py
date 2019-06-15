from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, validators
  
class LoginForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [validators.InputRequired()])
    password = PasswordField("Salasana", [validators.InputRequired()])
  
    class Meta:
        csrf = False


class RegisterForm(FlaskForm):
    username = StringField("Käyttäjätunnus", [validators.InputRequired()])
    password = PasswordField("Salasana", [validators.InputRequired()])        

    class Meta:
        csrf = False