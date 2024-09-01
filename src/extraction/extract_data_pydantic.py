import requests
from bs4 import BeautifulSoup
from pydantic import BaseModel, ValidationError

class Product(BaseModel):
    name: str
    price: float

def extract_from_web():
    response = requests.get('https://example.com/products')
    soup = BeautifulSoup(response.content, 'html.parser')

    products = []
    for item in soup.select('.product'):
        try:
            product = Product(
                name=item.select_one('.name').text,
                price=float(item.select_one('.price').text.replace('$', ''))
            )
            products.append(product)
        except ValidationError as e:
            print(f"Error de validación: {e}")

    return products
