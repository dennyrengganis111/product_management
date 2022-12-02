from app import app
from app.controller import productController,imageController

@app.route("/")
def index():
    return "Hello World"

@app.route("/product_lists", methods = ["GET"])
def product_lists():
    return productController.get_product_list()

@app.route("/product_variant/<id>", methods = ["GET"])
def variant_list_by_product_id(id):
    return productController.get_product_variant(id)

@app.route("/image_upload",methods = ["POST"])
def upload_image():
    return imageController.upload_image()