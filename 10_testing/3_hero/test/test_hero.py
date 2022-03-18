import unittest

from project.hero import Hero


class HeroTests(unittest.TestCase):
    username = "erinbedri"
    level = 10
    health = 100
    damage = 5

    enemy_username = "test"
    enemy_level = 10
    enemy_health = 100
    enemy_damage = 5

    def setUp(self):
        self.hero = Hero(self.username, self.level, self.health, self.damage)
        self.enemy = Hero(self.enemy_username, self.enemy_level, self.enemy_health, self.enemy_damage)
        self.strong_hero = Hero("Strong", 10, 500, 100)
        self.strong_enemy = Hero("Strong Enemy", 10, 500, 100)

    def test_init(self):
        self.assertEqual(self.username, self.hero.username)
        self.assertEqual(self.level, self.hero.level)
        self.assertEqual(self.health, self.hero.health)
        self.assertEqual(self.damage, self.hero.damage)

    def test_battle__when_username_equals_enemy_username__expect_exception(self):
        self.enemy.username = self.username
        with self.assertRaises(Exception) as context:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight yourself", str(context.exception))

    def test_battle__when_hero_health_zero__expect_value_error(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_battle__when_hero_health_negative__expect_value_error(self):
        self.hero.health = -1
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(context.exception))

    def test_battle__when_enemy_health_zero__expect_value_error(self):
        self.enemy.health = 0
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(context.exception))

    def test_battle__when_enemy_health_negative__expect_value_error(self):
        self.enemy.health = -1
        with self.assertRaises(ValueError) as context:
            self.hero.battle(self.enemy)
        self.assertEqual(f"You cannot fight {self.enemy.username}. He needs to rest", str(context.exception))

    def test_battle_draw(self):
        self.hero.health = 25
        self.enemy.health = 25
        expected = "Draw"
        actual = self.hero.battle(self.enemy)
        self.assertEqual(expected, actual)

    def test_battle_hero_win(self):
        res = self.strong_hero.battle(self.enemy)
        self.assertEqual("You win", res)
        self.assertEqual(455, self.strong_hero.health)
        self.assertEqual(-900, self.enemy.health)
        self.assertEqual(11, self.strong_hero.level)
        self.assertEqual(10, self.enemy.level)
        self.assertEqual(105, self.strong_hero.damage)
        self.assertEqual(5, self.enemy.damage)

    def test_battle_enemy_win(self):
        res = self.hero.battle(self.strong_enemy)
        self.assertEqual("You lose", res)

        self.assertEqual(455, self.strong_enemy.health)
        self.assertEqual(-900, self.hero.health)
        self.assertEqual(11, self.strong_enemy.level)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(105, self.strong_enemy.damage)
        self.assertEqual(5, self.hero.damage)

    def test_str(self):
        expected = f"Hero {self.username}: {self.level} lvl\n" \
               f"Health: {self.health}\n" \
               f"Damage: {self.damage}\n"
        actual = str(self.hero)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()