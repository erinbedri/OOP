import unittest

from project.vehicle import Vehicle


class VehicleTests(unittest.TestCase):
    valid_fuel = 100
    valid_horse_power = 150
    valid_capacity = valid_fuel
    valid_fuel_consumption = 1.25

    def setUp(self):
        self.vehicle = Vehicle(self.valid_fuel, self.valid_horse_power)

    def test_init(self):
        self.assertEqual(self.valid_fuel, self.vehicle.fuel)
        self.assertEqual(self.valid_capacity, self.vehicle.capacity)
        self.assertEqual(self.valid_horse_power, self.vehicle.horse_power)
        self.assertEqual(self.valid_fuel_consumption, self.vehicle.fuel_consumption)

    def test_drive__when_fuel_is_less_than_fuel_needed__expect_exception(self):
        kilometers = 100
        with self.assertRaises(Exception) as context:
            self.vehicle.drive(kilometers)
        self.assertEqual("Not enough fuel", str(context.exception))

    def test_drive__when_fuel_is_more_than_fuel_needed__expect_exception(self):
        kilometers = 10
        fuel_needed = kilometers * self.valid_fuel_consumption
        self.vehicle.drive(kilometers)
        self.assertEqual(self.valid_fuel - fuel_needed, self.vehicle.fuel)

    def test_refuel__when_fuel_plus_refuel_more_than_capacity(self):
        fuel = 10
        with self.assertRaises(Exception) as context:
            self.vehicle.refuel(fuel)
        self.assertEqual("Too much fuel", str(context.exception))

    def test_refuel__when_fuel_plus_refuel_less_than_capacity(self):
        fuel = 10
        self.vehicle.fuel = 25
        self.vehicle.refuel(fuel)
        self.assertEqual(25 + fuel, self.vehicle.fuel)

    def test_str(self):
        expected = f"The vehicle has {self.valid_horse_power} " \
               f"horse power with {self.valid_fuel} fuel left and {self.valid_fuel_consumption} fuel consumption"
        actual = str(self.vehicle)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
