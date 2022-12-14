from app import db
from app.model.product import Product
from datetime import datetime

class Variant(db.Model):
    variant_id = db.Column(db.BigInteger, primary_key = True, autoincrement = True)
    variant_name = db.Column(db.String(250),nullable = False)
    variant_size = db.Column(db.String(30), nullable = False)
    variant_metric = db.Column(db.String(10), nullable= True)
    variant_color = db.Column(db.String(30), nullable = True)
    logo = db.Column(db.String(150), nullable= True)
    product_id = db.Column(db.BigInteger, db.ForeignKey(Product.product_id))
    created_at = db.Column(db.DateTime, default = datetime.utcnow)
    updated_at = db.Column(db.DateTime, default = datetime.utcnow)
    status = db.Column(db.Boolean(),default= True)


    def __repr__(self):
        return '<Variant {}>'.format(self.variant_name)