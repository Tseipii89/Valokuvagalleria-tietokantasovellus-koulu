from application import db
from application.Base import Base

class Like(Base):
    
    __tablename__ = "like"
    __table_args__ = (
        db.PrimaryKeyConstraint('account_id', 'picture_id'),
    )

    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)
    picture_id = db.Column(db.Integer, db.ForeignKey("picture.id"), nullable=False)

    def __init__(self, account_id, picture_id):
        self.account_id = account_id
        self.picture_id = picture_id
