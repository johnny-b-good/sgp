import unittest
from src.heroine import Heroine
from pygame.sprite import Sprite
from pygame.rect import Rect


class HeroineTest(unittest.TestCase):
    def setUp(self):
        self.field = Sprite()
        self.field.rect = Rect(0, 0, 1000, 1000)

        self.heroine = Heroine(
            sprite_size=(50, 50),
            hitbox_size=(20, 20),
            speed = 10,
            focus_coefficient=0.5,
            lives=3,
            bombs=3,
            field_ref=self.field
        )

    def test_set_pos(self):
        self.heroine.pos = (100, 500)
        self.assertEqual(self.heroine.rect.center, (100, 500),
                         'Main rect\'s position was not updated')
        self.assertEqual(self.heroine.hitbox.rect.center, (100, 500),
                         'Hitbox rect\'s position was not updated')

    def test_move(self):
        self.heroine.pos = (100, 500)
        orthogonal_step = 10
        diagonal_step = 7

        tests = [
            (self.heroine.UP, (100, 500 - orthogonal_step), 'move up'),
            (self.heroine.DOWN, (100, 500 + orthogonal_step), 'move down'),
            (self.heroine.LEFT, (100 - orthogonal_step, 500), 'move left'),
            (self.heroine.RIGHT, (100 + orthogonal_step, 500), 'move right'),

            (self.heroine.LEFT_UP, (100 - diagonal_step, 500 - diagonal_step), 'move left-up'),
            (self.heroine.RIGHT_UP, (100 + diagonal_step, 500 - diagonal_step), 'move right-up'),
            (self.heroine.LEFT_DOWN, (100 - diagonal_step, 500 + diagonal_step), 'move left-up'),
            (self.heroine.RIGHT_DOWN, (100 + diagonal_step, 500 + diagonal_step), 'move right-down'),
        ]

        for test in tests:
            direction, expected_pos, error_message = test
            self.heroine.move(direction)
            self.assertEqual(self.heroine.pos, expected_pos, error_message)
            self.assertEqual(self.heroine.rect.center, expected_pos, error_message)
            self.assertEqual(self.heroine.hitbox.rect.center, expected_pos, error_message)
            self.heroine.pos = (100, 500)

    def test_move_to_boundary(self):
        hitbox_half = 10

        tests = [
            (self.heroine.UP, (500, 15), (500, 0 + hitbox_half), 'bump up'),
            (self.heroine.DOWN, (500, 985), (500, 1000 - hitbox_half), 'bump down'),
            (self.heroine.LEFT, (15, 500), (0 + hitbox_half, 500), 'bump left'),
            (self.heroine.RIGHT, (985, 500), (1000 - hitbox_half, 500), 'bump right'),

            (self.heroine.LEFT_UP, (15, 15), (0 + hitbox_half, 0 + hitbox_half), 'bump left-up'),
            (self.heroine.RIGHT_UP, (985, 15), (1000 - hitbox_half, 0 + hitbox_half), 'bump right-up'),
            (self.heroine.LEFT_DOWN, (15, 985), (0 + hitbox_half, 1000 - hitbox_half), 'bump left-up'),
            (self.heroine.RIGHT_DOWN, (985, 985), (1000 - hitbox_half, 1000 - hitbox_half), 'bump right-down'),
        ]

        for test in tests:
            direction, current_pos, expected_pos, error_message = test
            self.heroine.pos = current_pos
            self.heroine.move(direction)
            self.assertEqual(self.heroine.pos, expected_pos, error_message)
            self.assertEqual(self.heroine.rect.center, expected_pos, error_message)
            self.assertEqual(self.heroine.hitbox.rect.center, expected_pos, error_message)

    def test_focus(self):
        self.heroine.focus(True)
        self.assertEqual(self.heroine.is_focused, True, 'failed to set focused state')
        self.assertEqual(self.heroine.speed, 5, 'failed to change speed to focused state')

        self.heroine.focus(False)
        self.assertEqual(self.heroine.is_focused, False, 'failed to unset focused state')
        self.assertEqual(self.heroine.speed, 10, 'failed to change speed back to unfocused state')


    def test_focus_move(self):
        self.fail()

    def test_focus_shoot(self):
        self.fail()

    def test_hit(self):
        self.assertEqual(self.heroine.lives, 3)
        for lives_num in reversed(range(3)):
            self.heroine.hit()
            self.assertEqual(self.heroine.lives, lives_num)

    def test_bonus(self):
        self.fail()

    def test_shoot(self):
        self.fail()







if __name__ == '__main__':
    unittest.main()
