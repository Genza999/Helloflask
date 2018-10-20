from flask import Flask, jsonify

from models import Product

app = Flask(__name__)

products = []
products.append(Product(1, 'Water', 4))


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/products', methods=['GET'])
def get_all_products():
    json_products = [product.to_json() for product in products]
    return jsonify({'products': json_products})


if __name__ == '__main__':
    app.run(debug=True)
