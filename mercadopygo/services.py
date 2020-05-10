import json
from mercadopygo.product import Product


def get_products():
    products = []
    with open('mercadopygo/database.json', 'r', encoding='utf-8') as file:
        data = json.load(file)
        for product in data['products']:
            products.append(Product(**product))
        
    return products


def get_product_id(id):
    products = get_products()
    product = list(filter(lambda product: id == product.id , products))[0]

    return product
