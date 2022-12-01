from app.model.product import Product
from app.model.variant import Variant
from app.controller.FormatController import Format_get_product_list, Format_get_variant_from_product_id

from app import response, app, db
from flask import request

def get_product_list():
    try:
        products = Product.query.all()
        data = Format_get_product_list(products)
        return response.success(data, "success")

    except Exception as e:
        print(e)

def get_product_variant(id):
    try:
        product = Product.query.filter_by(product_id=id).first()
        variants =  Variant.query.filter(Variant.product_id == id)

        if not product:
            return response.badRequest([], "Product ID not found")
        data = Format_get_variant_from_product_id(variants,product.product_id)

        return response.success(data, "success")

    except Exception as e:
        print(e)