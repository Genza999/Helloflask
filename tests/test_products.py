import unittest
import json
from app import app


class TestProducts(unittest.TestCase):

    def setUp(self):
        self.app_tester = app.test_client()

    def test_all_products(self):
        input_data = {'id': 1, 'name': 'Phone', 'price': 200000}
        self.app_tester.post('/products', json=input_data)
        input_data = {'id': 2, 'name': 'Super', 'price': 30000}
        self.app_tester.post('/products', json=input_data)

        response = self.app_tester.get('/products')
        print(response)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(data['products']), 2)
        self.assertEqual(data['products'][0]['id'], 1)
        self.assertEqual(data['products'][0]['name'], 'Phone Number')

    def test_all_products_when_empty(self):
        response = self.app_tester.get('/products')
        print(response)
        data = json.loads(response.data)
        self.assertEqual(response.status_code, 400)
        self.assertIn('no products', data['message'])

    def test_add_products(self):
        input_data = {'id': 1, 'name': 'Phone', 'price': 2}
        response = self.app_tester.post('/products', json=input_data)
        self.assertEqual(response.status_code, 201)

    def test_add_product_wrong_price(self):
        input_data = {'id': 1, 'name': 'Phone', 'price': 'two'}
        response = self.app_tester.post('/products', json=input_data)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()