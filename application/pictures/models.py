from application import db
from application.Base import Base

from sqlalchemy.sql import text
from sqlalchemy import UniqueConstraint

hashtag_table = db.Table('hashtags', Base.metadata,
    db.Column('hashtag_id', db.Integer, db.ForeignKey('hashtag.id')),
    db.Column('picture_id', db.Integer, db.ForeignKey('picture.id')),
    UniqueConstraint('hashtag_id', 'picture_id', name='uix_1')
)


class Picture(Base):
    
    __tablename__ = "picture"
    
    date_taken = db.Column(db.DateTime, default=db.func.current_timestamp())
    path = db.Column(db.String(255), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)

    hashtags = db.relationship('Hashtag', secondary=hashtag_table, back_populates="pictures")
 
    def __init__(self, name):
        self.path = name   

    @staticmethod
    def get_hashtags():
        stmt = text("SELECT hashtag_id, hashtag.hashtag FROM hashtags" 
                    " LEFT JOIN hashtag ON hashtag.id = hashtag_id"
                    " LEFT JOIN picture ON picture.id = picture_id")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id": row[0],"nimi": row[1] })

        return response    


    @staticmethod
    def delete_hashtags(pic):
        stmt = text("DELETE FROM hashtags" 
                    " WHERE picture_id = :pic").params(pic=pic)
        res = db.engine.execute(stmt)    


class Hashtag(Base):
    
    __tablename__ = "hashtag"
    
    hashtag = db.Column(db.String(255), unique=True, nullable=False)
    pictures = db.relationship('Picture', secondary=hashtag_table, back_populates="hashtags")

    @staticmethod
    def find_hashtags(hash):
        stmt = text("SELECT id FROM hashtag" 
                    " WHERE hashtag = :hash").params(hash=hash)
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row[0])

        return response 
    
    def __init__(self, hashtag):
        self.hashtag = hashtag

        