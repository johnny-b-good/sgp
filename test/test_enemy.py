#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest
import pygame
from pygame.sprite import Sprite, Group
from pygame.rect import Rect

from src.enemy import Enemy
import src.resource_manager as resource_manager

# Init pygame and load resources
pygame.init()
pygame.display.set_mode((800, 600))
resource_manager.init()


class EnemeyTest(unittest.TestCase):
    def setUp(self):
        self.enemy_shots_group = Group()
        self.enemies_group = Group()

        self.params = {
            'pos': (100, 500),
            'sprite_size': (40, 40),
            'sprite_image': 'enemy.png',

            'health': 10,

            'sprite_groups': [self.enemies_group],
            'enemy_shots_groups': [self.enemy_shots_group],

            'movement_scenario': [],
            'shooting_scenario': [],
        }

        self.enemy = Enemy(self.params)

    def test_set_pos(self):
        self.fail()