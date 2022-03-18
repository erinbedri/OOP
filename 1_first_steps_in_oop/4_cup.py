class Cup:
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity

    def fill(self, amount):
        if self.size >= (self.quantity + amount):
            self.quantity += amount

    def status(self):
        free_space = self.size - self.quantity
        return free_space