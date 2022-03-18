from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit


class Mouse(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.weight_increase = 0.10
        self.suitable_food = [Fruit, Vegetable]

    def make_sound(self):
        return f"Squeak"


class Dog(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.weight_increase = 0.40
        self.suitable_food = [Meat]

    def make_sound(self):
        return f"Woof!"


class Cat(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.weight_increase = 0.30
        self.suitable_food = [Meat, Vegetable]

    def make_sound(self):
        return f"Meow"


class Tiger(Mammal):
    def __init__(self, name, weight, living_region):
        super().__init__(name, weight, living_region)
        self.weight_increase = 1.00
        self.suitable_food = [Meat]

    def make_sound(self):
        return f"ROAR!!!"

