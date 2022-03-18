from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    SUMMER_FUEL_CONSUMPTION_INCREASE = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
        self.summer_consumption = Car.SUMMER_FUEL_CONSUMPTION_INCREASE

    def drive(self, distance):
        self.fuel_consumption += self.summer_consumption
        if self.fuel_quantity >= (self.fuel_consumption * distance):
            self.fuel_quantity -= (distance * self.fuel_consumption)

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    SUMMER_FUEL_CONSUMPTION_INCREASE = 1.6
    TANK_HOLE_PERCENTAGE = 0.95

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__(fuel_quantity, fuel_consumption)
        self.summer_consumption = Truck.SUMMER_FUEL_CONSUMPTION_INCREASE

    def drive(self, distance):
        self.fuel_consumption += self.summer_consumption
        if self.fuel_quantity >= (self.fuel_consumption * distance):
            self.fuel_quantity -= (distance * self.fuel_consumption)

    def refuel(self, fuel):
        self.fuel_quantity += fuel * Truck.TANK_HOLE_PERCENTAGE