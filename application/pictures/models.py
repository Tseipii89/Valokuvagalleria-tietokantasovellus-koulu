from application import db
from application.Base import Base

from sqlalchemy.sql import text

hashtag_table = db.Table('hashtags', Base.metadata,
    db.Column('hashtag_id', db.Integer, db.ForeignKey('hashtag.id')),
    db.Column('picture_id', db.Integer, db.ForeignKey('picture.id'))
)


class Picture(Base):
    
    __tablename__ = "picture"
    
    date_taken = db.Column(db.DateTime, default=db.func.current_timestamp())
    path = db.Column(db.String(255), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)

    hashtags = db.relationship('Hashtag', secondary=hashtag_table, back_populates="pictures")

    def __init__(self, name):
        self.path = name   


class Hashtag(Base):
    
    __tablename__ = "hashtag"
    
    hashtag = db.Column(db.String(255), unique=True, nullable=False)
    pictures = db.relationship('Picture', secondary=hashtag_table, back_populates="hashtags")

    def __init__(self, hashtag):
        self.hashtag = hashtag

        