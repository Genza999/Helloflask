from flask import Flask, jsonify, request

from models import Product

app = Flask(__name__)

products = []


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/products', methods=['GET'])
def get_all_products():
    json_products = []
    print(products)
    for product in products:
        json_products.append(product.to_json())

    print(json_products)
    print(len(json_products))
    if len(json_products) < 1:
        return jsonify({'message': 'There are no products'}), 400
    return jsonify({'products': json_products}), 200


@app.route('/products', methods=['POST'])
def add_product():
    data = request.get_json()
    print(data)
    product = Product(data['id'], data['name'], data['price'])
    products.append(product)
    return jsonify({'products': [product.to_json()]}), 201


if __name__ == '__main__':
    app.run(debug=True)
