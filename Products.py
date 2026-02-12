from fastapi import FastAPI
from model import Product

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
