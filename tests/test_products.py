import unittest
import json
from app import app


class TestProducts(unittest.TestCase):

    def setUp(self):
        self.app_tester = app.test_client()

    def test_dictionary_response(self):
        response = self.app_tester.get('http://127.0.0.1:5000/products')
        print(response)
        self.assertEqual(response.status_code, 400)


if __name__ == '__main__':
    unittest.main()