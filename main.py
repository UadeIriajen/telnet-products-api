from fastapi import FastAPI
from model import Product
from database import session 
app = FastAPI()

@app.get("/")
def greet():
    return {"message": "Telnet Company"}

products = [
    Product(
        id=1,
        name="phone",
        description="A smartphone",
        price=99,
        quantity=10
    ),
    Product(
        id=2,
        name="laptop",
        description="A powerful laptop",
        price=999,
        quantity=100
    ),
    Product(
        id=3, 
        name="Pen",
        description="A blue ink pen",
        price=1.99,
        quantity=100
    ),
    Product(
        id=4,
        name="Table", 
        description="A wooden table", 
        price=199.99, 
        quantity=20
        ),
]


@app.get("/products")
def get_all_products():
    db = session()
    db.query(Product).all()
    return products


@app.get("/products/{product_id}")
def get_product_by_id(product_id: int):
    for product in products:
        if product.id == product_id:
            return product
    return {"error": "Product not found"}

@app.post("/product")
def add_product(product: Product):
    products.append(product)
    return {"message": "Product added successfully", "product": product}

@app.put("/products/{product_id}")
def update_products(product_id : int, updated_product: Product):
    for i in range(len(products)):
        if products[i].id == product_id:
            products[i] = updated_product
            return {"message": "Product updated successfully", "product": updated_product}
    
    return {"error": "Product not found"}

@app.delete("/products/{product_id}")
def delete_product(product_id: int):
    for i in range(len(products)):
        if products[i].id == product_id:
            del products[i]
            return "Product deleted" 
    
    return "Product not found"

