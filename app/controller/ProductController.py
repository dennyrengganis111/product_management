from app.model.product import Product
from app.model.variant import Variant
from app.model.image import Image
from app.controller.utilController import Format_get_product_list, Format_get_variant_from_product_id, validate_upload_product, validate_file_ext, Format_get_images_from_product_id

from app import response, app, db
from flask import request
import os, uuid
from werkzeug.utils import secure_filename

def get_product_list():
    # try:
    products = Product.query.all()
    data = Format_get_product_list(products)
    return response.success(data, "success")

    # except Exception as e:
    #     print(e)

def get_product_variant(id):
    try:
        product = Product.query.filter_by(product_id=id).first()
        if not product:
            return response.badRequest([], "Product ID not found")

        variants =  Variant.query.filter(Variant.product_id == id)
        data = Format_get_variant_from_product_id(variants,product.product_id)

        return response.success(data, "success")

    except Exception as e:
        print(e)

def get_stored_image_under_product(id):
    try:
        product = Product.query.filter_by(product_id=id).first()
        if not product:
            return response.badRequest([],"Product ID not found")
        images = Image.query.filter(Image.item_id == id, Image.item_type == "product")
        data = Format_get_images_from_product_id(images,product.product_id)
        return response.success(data, "success")
    except Exception as e:
        print(e)

def upload_product():
    try:
        err = validate_upload_product(request)
        if err :
            return response.badRequest([], err)
        
        product_name = request.form.get("product_name")
        product_description = request.form.get("product_description")
        created_at = request.form.get("created_at")
        updated_at = request.form.get("updated_at")

        if "image" in request.files and request.files["image"].filename != "" and validate_file_ext(request.files["image"].filename):
            filename = secure_filename(request.files["image"].filename)
            uid = uuid.uuid4()
            stored_logo = "LOGO"+str(uid)+filename
        else:
            stored_logo = ""
        products = Product(product_name = product_name, product_description = product_description,
        logo= stored_logo, created_at= created_at, updated_at = updated_at)

        db.session.add(products)
        db.session.commit()

        if stored_logo:
            request.files["image"].save(os.path.join(app.config["UPLOAD_FOLDER"],stored_logo))

        return response.success({"product_name": product_name}, "product successfully created")
        
    except Exception as e:
        print(e)