import unittest
import pygame
from pygame.sprite import Sprite
from pygame.rect import Rect

from src.projectile import Projectile
from src.movement import linear
import src.resource_manager as resource_manager

# Init pygame and load resources
pygame.init()
pygame.display.set_mode((800, 600))
resource_manager.init()


class ProjectileTest(unittest.TestCase):
    def setUp(self):
        Projectile.setup_class_attrs({
            'image_id': 'shot1.png',
            'func': None,
            'size': (10, 20),
            'damage': 100
        })

        self.projectile = Projectile({
            'pos': (100, 500),
        })

    def test_pos(self):
        self.assertEqual(self.projectile.pos, (100, 500), 'start')

    def test_linear_1(self):
        Projectile.func = linear(angle=0, speed=200)
        self.projectile.update(500)
        self.assertEqual(self.projectile.pos, (200, 500), 'right')

    def test_linear_2(self):
        Projectile.func = linear(angle=90, speed=200)
        self.projectile.update(500)
        self.assertEqual(self.projectile.pos, (100, 400), 'up')
