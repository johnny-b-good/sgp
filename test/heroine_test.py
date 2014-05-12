import unittest
from src.heroine import Heroine
from pygame import sprite

class HeroineTest(unittest.TestCase):
    def setUp(self):
        self.heroine = Heroine()

    def test_hit(self):
        self.heroine.hit()
        self.assertEqual(self.heroine.lives, 2)

    def test_shoot(self):
        self.fail()

    def test_invulnerable(self):
        self.fail()


class HeroineFocus(unittest.TestCase):
    def setUp(self):
        self.heroine = Heroine()

    def test_focus_true(self):
        self.heroine.focus(True)
        self.assertEqual(self.heroine.is_focused, True)
        self.assertEqual(self.heroine.speed, self.heroine.base_speed / 2)

    def test_focus_false(self):
        self.heroine.focus(False)
        self.assertEqual(self.heroine.is_focused, False)
        self.assertEqual(self.heroine.speed, self.heroine.base_speed)

    def test_focus_move(self):
        self.fail()

    def test_focus_shoot(self):
        self.fail()


class HeroineMove(unittest.TestCase):
    def setUp(self):
        self.heroine = Heroine()
        self.heroine.pos = (100, 500)
        self.heroine.speed = 10

    def test_set_pos(self):
        self.assertEqual(self.heroine.rect.center, (100, 500))
        self.assertEqual(self.heroine.hitbox.rect.center, (100, 500))

    def _test_move(self, expected_pos):
        self.assertEqual(self.heroine.pos, expected_pos)
        self.assertEqual(self.heroine.rect.center, expected_pos)
        self.assertEqual(self.heroine.hitbox.rect.center, expected_pos)

    def test_move_up(self):
        self.heroine.move(self.heroine.UP)
        expected_pos = (100, 500 - self.heroine.speed)
        self._test_move(expected_pos)

    def test_move_down(self):
        self.heroine.move(self.heroine.DOWN)
        expected_pos = (100, 500 + self.heroine.speed)
        self._test_move(expected_pos)

    def test_move_left(self):
        self.heroine.move(self.heroine.LEFT)
        expected_pos = (100 - self.heroine.speed, 500)
        self._test_move(expected_pos)

    def test_move_right(self):
        self.heroine.move(self.heroine.RIGHT)
        expected_pos = (100 + self.heroine.speed, 500)
        self._test_move(expected_pos)

    def test_top_boundary(self):
        self.heroine.move(self.heroine.UP)
        self.fail()

    def test_bottom_boundary(self):
        self.heroine.move(self.heroine.DOWN)
        self.fail()

    def test_left_boundary(self):
        self.heroine.move(self.heroine.LEFT)
        self.fail()

    def test_right_boundary(self):
        self.heroine.move(self.heroine.RIGHT)
        self.fail()

class HeroineBonus(unittest.TestCase):
    def setUp(self):
        self.heroine = Heroine()

    def test_bonus_bomb(self):
        self.fail()

    def test_bonus_live(self):
        self.fail()

    def test_bonus_power(self):
        self.fail()

    def test_bonus_score(self):
        self.fail()



if __name__ == '__main__':
    unittest.main()
