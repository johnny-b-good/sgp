import unittest
import pygame
from pygame.sprite import Sprite
from pygame.rect import Rect

from src.projectile import Projectile
from src.movement_functions import linear

pygame.init()
DISPLAY_SURF = pygame.display.set_mode((800, 600))


class ProjectileTest(unittest.TestCase):
    def setUp(self):
        self.params = {
            'pos': (100, 500),
            'size': (10, 20),
            'image': '../src/gfx/shot1.png',
            'func': None
        }
        self.projectile = Projectile(self.params)

    def test_linear(self):
        self.assertEqual(self.projectile.pos, (100, 500), 'start')

        self.projectile.func = linear(angle=0, speed=200)
        self.projectile.update(500)
        self.assertEqual(self.projectile.pos, (200, 500), 'right')

        self.projectile.func = linear(angle=90, speed=200)
        self.projectile.update(500)
        self.assertEqual(self.projectile.pos, (200, 400), 'up')

        self.projectile.func = linear(angle=180, speed=200)
        self.projectile.update(500)
        self.assertEqual(self.projectile.pos, (100, 400), 'left')

        self.projectile.func = linear(angle=270, speed=200)
        self.projectile.update(500)
        self.assertEqual(self.projectile.pos, (100, 500), 'down')