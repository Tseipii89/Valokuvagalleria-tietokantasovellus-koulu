from application import db

class Picture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    date_taken = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
    onupdate=db.func.current_timestamp())

    path = db.Column(db.String(255), nullable=False)

    account_id = db.Column(db.Integer, db.ForeignKey("account.id"), nullable=False)

    def __init__(self, name):
        self.path = name

        