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

def Product_db_to_dict(product):
    product_dict = {
        "product_id" : product.product_id,
        "product_name" : product.product_name,
        "product_description" : product.product_description,
        "logo_id" : product.logo_id,
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
        "logo_id" : variant.logo_id,
        "created_at" : variant.created_at,
        "updated_at" : variant.updated_at
    }
    return variant_dict