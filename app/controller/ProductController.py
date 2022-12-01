from app.model.product import Product

from app import response, app, db
from flask import request

def index():
    try:
        products = Product.query.all()
        data = format(products)
        return response.success(data, "success")

    except Exception as e:
        return response.badRequest("", "failed")

def format(products):
    datas = []
    for product in products:
        datas.append(db_to_dict(product))
    return datas

def db_to_dict(product):
    product_dict = {
        "product_id" : product.product_id,
        "product_name" : product.product_name,
        "product_description" : product.product_description,
        "logo_id" : product.logo_id,
        "created_at" : product.created_at,
        "updated_at" : product.updated_at
        
    }
    return product_dict