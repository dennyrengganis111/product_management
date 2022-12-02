from app import app
from app.controller import productController,imageController, variantController
from app import const
from flask import request

@app.route("/")
def index():
    return "Hello World"


@app.route(const.GetProductByID,
methods = ["GET","PUT"])
def get_product_by_id(id):
    if request.method == "GET":
        return productController.get_product_by_id(id)
    elif request.method == "PUT":
        return productController.edit_product_by_id(id)


@app.route(const.GetVariantByID,
methods = ["GET","PUT"])
def get_variant_by_id(id):
    if request.method == "GET":
        return variantController.get_variant_by_id(id)
    elif request.method == "PUT":
        return variantController.edit_variant_by_id(id)


@app.route(const.GetProductList,
methods = ["GET"])
def product_lists():
    return productController.get_product_list()

@app.route(const.GetVariantListByProductID,
methods = ["GET"])
def variant_list_by_product_id(id):
    return productController.get_product_variant(id)

@app.route(const.GetImageListByProductID,
methods = ["GET"])
def image_list_by_product_id(id):
    return productController.get_stored_image_under_product(id)

@app.route(const.GetImageListByVariantID,
methods = ["GET"])
def image_list_by_variant_id(id):
    return variantController.get_stored_image_under_variant(id)

@app.route(const.ImageUpload,
methods = ["POST"])
def upload_image():
    return imageController.upload_image()

@app.route(const.ProductUpload,
methods = ["POST"])
def upload_product():
    return productController.upload_product()

@app.route(const.VariantUpload,
methods = ["POST"])
def upload_variant():
    return variantController.upload_variant()

@app.route(const.DeleteImageByID,
methods = ["PUT"])
def delete_image(id):
    return imageController.delete_image(id)

@app.route(const.DeleteVariantByID,
methods = ["PUT"])
def delete_variant(id):
    return variantController.delete_variant(id)

@app.route(const.DeleteProductByID,
methods = ["PUT"])
def delete_product(id):
    return productController.delete_product_by_id(id)