from application import db
from application.Base import Base


class Picture(Base):
    
    __tablename__ = "picture"
    
    date_taken = db.Column(db.DateTime, default=db.func.current_timestamp())
    path = db.Column(db.String(255), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)

    def __init__(self, name):
        self.path = name


        