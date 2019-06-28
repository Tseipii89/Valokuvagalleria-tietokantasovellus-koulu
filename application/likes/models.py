from application import db
from application.Base import Base

from sqlalchemy.sql import text

class Like(db.Model):
    
    __tablename__ = "liked"
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
        stmt = text("SELECT picture_id, COUNT(*) FROM liked GROUP BY picture_id;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append({"id": row[0], "count": row[1]})

        return response
     
    @staticmethod
    def pic_delete(pic_id):
        stmt = text("DELETE FROM liked WHERE picture_id = :pic_id;").params(pic_id = pic_id)
        res = db.engine.execute(stmt)

        return res 

    @staticmethod
    def find_users_with_like():
        stmt = text("SELECT account_id, picture_id FROM liked;")
        res = db.engine.execute(stmt)

        response = []
        for row in res:
            response.append((row[0], row[1]))

        return response    


    def __init__(self, account_id, picture_id):
        self.account_id = account_id
        self.picture_id = picture_id
