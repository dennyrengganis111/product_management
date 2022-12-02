from app.model.product import Product
from app.model.variant import Variant
from app.controller.utilController import validate_upload_variant,validate_file_ext

from app import response, app, db
from flask import request
import os, uuid
from werkzeug.utils import secure_filename


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