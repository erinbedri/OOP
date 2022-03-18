from project.mammal import Mammal
import unittest


class MammalTests(unittest.TestCase):
    valid_name = "Bear"
    valid_type = "carnivore"
    valid_sound = "rohr"
    valid_kingdom = "animals"

    def setUp(self):
        self.mammal = Mammal(self.valid_name, self.valid_type, self.valid_sound)

    def test_init__when_valid__expect_initialization(self):
        self.assertEqual(self.valid_name, self.mammal.name)
        self.assertEqual(self.valid_type, self.mammal.type)
        self.assertEqual(self.valid_sound, self.mammal.sound)
        self.assertEqual(self.valid_kingdom, self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        expected_result = f"{self.valid_name} makes {self.valid_sound}"
        actual_result = self.mammal.make_sound()
        self.assertEqual(expected_result, actual_result)

    def test_get_kingdom(self):
        expected_result = self.valid_kingdom
        actual_result = self.mammal.get_kingdom()
        self.assertEqual(expected_result, actual_result)

    def test_info(self):
        expected_result = f"{self.valid_name} is of type {self.valid_type}"
        actual_result = self.mammal.info()
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    unittest.main()