from app import app
from app.controller import productController,imageController, variantController

@app.route("/")
def index():
    return "Hello World"

@app.route("/product_lists", methods = ["GET"])
def product_lists():
    return productController.get_product_list()

@app.route("/product_variant/<id>", methods = ["GET"])
def variant_list_by_product_id(id):
    return productController.get_product_variant(id)

@app.route("/image_list_by_product_id/<id>", methods = ["GET"])
def image_list_by_product_id(id):
    return productController.get_stored_image_under_product(id)

@app.route("/image_list_by_variant_id/<id>", methods = ["GET"])
def image_list_by_variant_id(id):
    return variantController.get_stored_image_under_variant(id)

@app.route("/image_upload",methods = ["POST"])
def upload_image():
    return imageController.upload_image()

@app.route("/product_upload", methods = ["POST"])
def upload_product():
    return productController.upload_product()

@app.route("/variant_upload", methods = ["POST"])
def upload_variant():
    return variantController.upload_variant()