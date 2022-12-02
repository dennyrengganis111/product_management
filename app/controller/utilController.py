def Format_get_product_list(products):
    datas = []
    for product in products:
        datas.append(Product_db_to_dict(product))
    return datas



def Format_get_variant_from_product_id(variants,product_id):
    datas = {
        "product_id": product_id,
        "variants" : []
    }
    for variant in variants:
        datas["variants"].append(Variant_db_to_dict(variant))
    
    return datas


def Format_get_images_from_product_id(images, product_id):
    datas = {
        "product_id": product_id,
        "images" : []
    }
    for image in images:
        datas["images"].append(Image_db_to_dict(image))
    return datas

def Format_get_images_from_variant_id(images, variant_id):
    datas = {
        "variant_id": variant_id,
        "images" : []
    }
    for image in images:
        datas["images"].append(Image_db_to_dict(image))
    return datas

def Image_db_to_dict(image):
    image_dict = {
        "image_id" : image.image_id,
        "image_name" : image.image_name,
        "image_path" : image.image_path,
        "created_at" : image.created_at,
        "updated_at" : image.updated_at
    }

    return image_dict

def Product_db_to_dict(product):
    product_dict = {
        "product_id" : product.product_id,
        "product_name" : product.product_name,
        "product_description" : product.product_description,
        "logo_id" : product.logo,
        "created_at" : product.created_at,
        "updated_at" : product.updated_at
        
    }
    return product_dict

def Variant_db_to_dict(variant):
    variant_dict = {
        "variant_id" : variant.variant_id,
        "variant_name" : variant.variant_name,
        "variant_size" : variant.variant_size,
        "variant_metric" : variant.variant_metric,
        "variant_color" : variant.variant_color,
        "logo_id" : variant.logo,
        "created_at" : variant.created_at,
        "updated_at" : variant.updated_at
    }
    return variant_dict

def validate_file_ext(filename):
    allowed_ext = ["jpg","jpeg","png"]
    if filename.split(".")[-1] not in allowed_ext:
        return False
    return True


def validate_upload_image_request(request):
    if "image" not in request.files:
        return "image file not found"
    file = request.files["image"]
    if file.filename == "":
        return "image file not found"
    
    if "item_id" not in request.form:
        return "item_id for image not found"
    
    if "item_type" not in request.form:
        return "item_type not found"
    
def validate_upload_product(request):
    if "product_name" not in request.form:
        return "product name is not filled"
    
def validate_upload_variant(request):
    if "variant_name" not in request.form:
        return "variant name is not filled"
    if "variant_size" not in request.form:
        return "variant size is not filled"
    if "product_id" not in request.form:
        return "product id of variant is not filled"
    