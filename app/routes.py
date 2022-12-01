from app import app
from app.controller import ProductController

@app.route("/")
def index():
    return "Hello World"

@app.route("/product_lists", methods = ["GET"])
def product_lists():
    return ProductController.get_product_list()

@app.route("/product_variant/<id>", methods = ["GET"])
def variant_list_by_product_id(id):
    return ProductController.get_product_variant(id)