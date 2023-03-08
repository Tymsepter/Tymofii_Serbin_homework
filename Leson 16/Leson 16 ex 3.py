class Product:
    def __init__(self, type, name, price):
        self.type = type
        self.name = name
        self.price = price


class ProductStore:
    def __init__(self):
        self.products = {}

    def add(self, product, amount):
        if not isinstance(product, Product):
            raise ValueError("Invalid product")
        if product.name not in self.products:
            self.products[product.name] = {"product": product, "amount": 0}
        self.products[product.name]["amount"] += amount
