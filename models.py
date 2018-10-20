class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def to_json(self):
        return {'id': self.id, 'name': self.name, 'price': self.price}