from app.model.product import Product
from app.model.variant import Variant
from app.model.image import Image
from app.controller.utilController import validate_upload_variant,validate_file_ext, Format_get_images_from_variant_id, Variant_db_to_dict

from app import response, app, db
from flask import request
import os, uuid
from werkzeug.utils import secure_filename

def get_variant_by_id(id):
    try:
        variant = Variant.query.filter_by(variant_id = id).first()
        if not variant:
            return response.badRequest([], "Variant ID not found")
        variant_dict = Variant_db_to_dict(variant)
        return response.success(variant_dict, "Success")
    except Exception as e:
        print(e) 

def get_stored_image_under_variant(id):
    try:
        variant = Variant.query.filter_by(variant_id=id).first()
        if not variant:
            return response.badRequest([],"Variant ID not found")
        images = Image.query.filter(Image.item_id == id, Image.item_type == "variant")
        data = Format_get_images_from_variant_id(images,variant.product_id)
        return response.success(data, "success")
    except Exception as e:
        print(e)


def upload_variant():
    try:
        err = validate_upload_variant(request)
        if err:
            return response.badRequest([],err)
        
        product = Product.query.filter_by(product_id=request.form["product_id"]).first()
        if not product:
            return response.badRequest([],"can't created variant under non existing product id")
        
        variant_name = request.form.get("variant_name")
        variant_size = request.form.get("variant_size")
        variant_metric = request.form.get("variant_metric")
        variant_color = request.form.get("variant_color")
        product_id = request.form.get("product_id")
        created_at = request.form.get("created_at")
        updated_at = request.form.get("updated_at")

        if "image" in request.files and request.files["image"].filename != "" and validate_file_ext(request.files["image"].filename):
            filename = secure_filename(request.files["image"].filename)
            uid = uuid.uuid4()
            stored_logo = "LOGO-VARIANT"+str(uid)+filename
        else:
            stored_logo = ""
        variants = Variant(variant_name = variant_name, variant_size= variant_size, variant_metric = variant_metric,
        variant_color = variant_color, product_id = product_id, logo = stored_logo , created_at= created_at, updated_at = updated_at)


        db.session.add(variants)
        db.session.commit()

        if stored_logo:
            request.files["image"].save(os.path.join(app.config["UPLOAD_FOLDER"],stored_logo))

        return response.success({"variant_name": variant_name, "product_id": product_id}, "variant successfully created")
    except Exception as e:
        print(e)

def edit_variant_by_id(id):
    try:
        variant = Variant.query.filter_by(variant_id=id).first()
        if not variant:
            return response.badRequest([],"Variant ID not found")
        
        variant_name = request.form.get("variant_name")
        variant_size = request.form.get("variant_size")
        variant_metric = request.form.get("variant_metric")
        variant_color = request.form.get("variant_color")

        if "image" in request.files and request.files["image"].filename != "" and validate_file_ext(request.files["image"].filename):
            filename = secure_filename(request.files["image"].filename)
            uid = uuid.uuid4()
            stored_logo = "LOGO-VARIANT"+str(uid)+filename
        else:
            stored_logo = ""
        
        if variant_name:
            variant.variant_name = variant_name
        if variant_size:
            variant.variant_size = variant_size
        if variant_metric:
            variant.variant_metrict = variant_metric
        if variant_color:
            variant.variant_color = variant_color
        
        old_image = ""
        if stored_logo:
            if variant.logo:
                old_image = os.path.join(app.config["UPLOAD_FOLDER"], variant.logo)
            variant.logo = stored_logo

        db.session.commit()

        if stored_logo:
            if os.path.exists(old_image) and variant.logo:
                os.remove(old_image)   
            request.files["image"].save(os.path.join(app.config["UPLOAD_FOLDER"],stored_logo))
        data = {
            "variant_id": variant.variant_id,
            "variant_name": variant.variant_name,
            "variant_size": variant.variant_size,
            "variant_metric" : variant.variant_metric,
            "variant_color": variant.variant_color,
            "logo_path": stored_logo
        }
        return response.success(data, "Varaint updated")
    except Exception as e:
        print(e)