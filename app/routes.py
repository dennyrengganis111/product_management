from app import app
from app.controller import ProductController

@app.route("/")
def index():
    return "Hello World"

@app.route("/product_lists", methods = ["GET"])
def product_lists():
    return ProductController.index()