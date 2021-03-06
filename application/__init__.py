from flask import Flask
app = Flask(__name__)

from flask_sqlalchemy import SQLAlchemy

# Eritetään tuontanto ja kehitysympäristö
import os

if os.environ.get("HEROKU"):
    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///gallery.db"    
    app.config["SQLALCHEMY_ECHO"] = True 

# Luodaan db-olio, jota käytetään tietokannan käsittelyyn
db = SQLAlchemy(app)

# Luetaan kansiosta application tiedoston views sisältö
from application import views

# Tuodaan pictures tietokanta
from application.pictures import models
from application.pictures import views

# Tuodaan auth tietokanta

from application.auth import models
from application.auth import views

#Kirjautuminen
from application.auth.models import User
from os import urandom
app.config["SECRET_KEY"] = urandom(32)

from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = "auth_login"
login_manager.login_message = "Kirjaudu sisään käyttääksesi tätä toiminnallisuutta."

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

# Tuodaan tykkäykset
from application.likes import models

# Luodaan lopulta tarvittavat tietokantataulut
try:
    db.create_all()
except:
    pass    
