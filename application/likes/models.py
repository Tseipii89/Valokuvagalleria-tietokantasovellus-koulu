from application import db
from application.Base import Base

from sqlalchemy.sql import text

class Like(db.Model):
    
    __tablename__ = "like"
    __table_args__ = (
        db.PrimaryKeyConstraint('account_id', 'picture_id'),
    )

    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
        onupdate=db.func.current_timestamp())

    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
    picture_id = db.Column(db.Integer, db.ForeignKey("picture.id"), nullable=False)


    @staticmethod
    def how_many_likes():
        stmt = text("SELECT COUNT(*) FROM 'like';")
        res = db.engine.execute(stmt)

        
        for row in res:
            response = row[0]

        return response 

    @staticmethod
    def find_users_with_like():
        stmt = text("SELECT 'account_id' FROM 'like';")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append(row[0])

        return response    


    def __init__(self, account_id, picture_id):
        self.account_id = account_id
        self.picture_id = picture_id
