class Product:
    def __init__(self, id, name, description, price, quantity, image):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.quantity = quantity
        self.image = image

    def __repr__(self):
        return f"Product({self.id}, {self.name}, {self.description}, {self.price}, {self.quantity}, {self.image}, )"