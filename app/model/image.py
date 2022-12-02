from app import db
from datetime import datetime

class Image(db.Model):
    image_id = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
    image_name = db.Column(db.String(250),nullable = False)
    item_type = db.Column(db.String(50), nullable = False)
    item_id = db.Column(db.Integer, nullable = False)
    image_path = db.Column(db.String(150), nullable = False)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)


    def __repr__(self):
        return '<Image {}>'.format(self.image_name)