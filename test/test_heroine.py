import unittest
import pygame
from pygame.sprite import Sprite, Group
from pygame.rect import Rect
from src.heroine import Heroine
from src.helpers import *


class HeroineTest(unittest.TestCase):
    def setUp(self):
        self.field = Sprite()
        self.field.rect = Rect(0, 0, 1000, 1000)
        self.shots_group = Group()

        self.params = {
            'pos': (100, 500),
            'sprite_size': (50, 50),
            'hitbox_size': (20, 20),
            'sprite_image': image_path('reimu.png'),
            'hitbox_image': image_path('hitbox.png'),
            'speed': 10,
            'focus_coefficient': 0.5,
            'lives': 3,
            'bombs': 3,

            'playfield': self.field,
            'heroine_shots_groups': [self.shots_group],
        }

        self.heroine = Heroine(self.params)

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
            (self.heroine.UP, (100, 500 - orthogonal_step), 1000, 'move up'),
            (self.heroine.DOWN, (100, 500 + orthogonal_step), 1000,  'move down'),
            (self.heroine.LEFT, (100 - orthogonal_step, 500), 1000,  'move left'),
            (self.heroine.RIGHT, (100 + orthogonal_step, 500), 1000,  'move right'),

            (self.heroine.LEFT_UP, (100 - diagonal_step, 500 - diagonal_step), 1000,  'move left-up'),
            (self.heroine.RIGHT_UP, (100 + diagonal_step, 500 - diagonal_step), 1000,  'move right-up'),
            (self.heroine.LEFT_DOWN, (100 - diagonal_step, 500 + diagonal_step), 1000,  'move left-up'),
            (self.heroine.RIGHT_DOWN, (100 + diagonal_step, 500 + diagonal_step), 1000,  'move right-down'),
        ]

        for test in tests:
            angle, expected_pos, time, error_message = test
            self.heroine.move(angle, time)
            self.assertEqual(self.heroine.pos, expected_pos, error_message)
            self.assertEqual(self.heroine.rect.center, expected_pos, error_message)
            self.assertEqual(self.heroine.hitbox.rect.center, expected_pos, error_message)
            self.heroine.pos = (100, 500)

    def test_move_to_boundary(self):
        hitbox_half = 10

        tests = [
            (self.heroine.UP, (500, 15), (500, 0 + hitbox_half), 1000,  'bump up'),
            (self.heroine.DOWN, (500, 985), (500, 1000 - hitbox_half), 1000,  'bump down'),
            (self.heroine.LEFT, (15, 500), (0 + hitbox_half, 500), 1000,  'bump left'),
            (self.heroine.RIGHT, (985, 500), (1000 - hitbox_half, 500), 1000,  'bump right'),

            (self.heroine.LEFT_UP, (15, 15), (0 + hitbox_half, 0 + hitbox_half), 1000,  'bump left-up'),
            (self.heroine.RIGHT_UP, (985, 15), (1000 - hitbox_half, 0 + hitbox_half), 1000,  'bump right-up'),
            (self.heroine.LEFT_DOWN, (15, 985), (0 + hitbox_half, 1000 - hitbox_half), 1000,  'bump left-up'),
            (self.heroine.RIGHT_DOWN, (985, 985), (1000 - hitbox_half, 1000 - hitbox_half), 1000,  'bump right-down'),
        ]

        for test in tests:
            angle, current_pos, expected_pos, time,  error_message = test
            self.heroine.pos = current_pos
            self.heroine.move(angle, time)
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
        self.assertEqual(len(self.heroine.heroine_shots_groups[0]), 0, 'Shots group wasn\'t empty at start')
        # self.heroine.shoot(1000)
        # print self.heroine.shots_group_ref
        # self.assertEqual(len(self.heroine.shots_group_ref), 5, 'There should be 5 shots after 1 second of shooting')
        self.fail()








if __name__ == '__main__':
    unittest.main()
