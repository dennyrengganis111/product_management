from app.model.image import Image
from app.controller.utilController import validate_file_ext, validate_upload_image_request

from app import response, app, db
from flask import request

import os
import uuid
from werkzeug.utils import secure_filename

from datetime import datetime

def upload_image():
    try:
        err = validate_upload_image_request(request)
        if err:
            return response.badRequest([], err)

        item_id = request.form.get("item_id")
        item_type = request.form.get("item_type")
        created_at = request.form.get("created_at")
        updated_at = request.form.get("updated_at")

        file = request.files["image"]

        if file and validate_file_ext(file.filename):
            filename = secure_filename(file.filename)
            uid = uuid.uuid4()
            stored_filename = str(uid)+filename
            

            uploads = Image(image_name = filename, image_path = stored_filename,item_id= item_id, item_type = item_type
            ,created_at = created_at, updated_at = updated_at)

            db.session.add(uploads)
            db.session.commit()

            file.save(os.path.join(app.config["UPLOAD_FOLDER"],stored_filename))

            return response.success({"image_name": filename, "pathname" :stored_filename},"success upload image")
        
        else:
            return response.badRequest([],"file extension is not allowed")
    except Exception as e:
        print(e)

