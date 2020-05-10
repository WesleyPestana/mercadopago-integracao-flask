from mercadopygo import services
from mercadopygo.api_mercadopago import payment
from flask import Flask, render_template, request, redirect


app = Flask(__name__)


@app.route('/')
def index():
    products = services.get_products()
    return render_template('products.html', products=products)


@app.route('/buy/<int:id_product>')
def buy_product(id_product):
    product = services.get_product_id(id_product)
    return redirect(payment(request, product=product))


if __name__ == "__main__":
    app.run(debug=True, port=5000)
