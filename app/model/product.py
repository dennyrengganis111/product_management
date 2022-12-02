from app import db
from datetime import datetime

class Product(db.Model):
    product_id = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
    product_name = db.Column(db.String(250),nullable = False)
    product_description = db.Column(db.String(1000), nullable = True)
    logo = db.Column(db.String(150), nullable= True)
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)


    def __repr__(self):
        return '<Product {}>'.format(self.product_name)