#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite
from pygame.rect import Rect

from helpers import *
import movement


class Projectile(Sprite):
    """Abstract projectile class

    You should not use it normally, make a subclass, will ya?
    """

    @classmethod
    def setup_class_attrs(cls, params):
        """Setup class attributes"""
        cls.func = params['func']
        cls.image = pygame.image.load(params['image']).convert()
        cls.size = params['size']

    def __init__(self, params):
        super(Projectile, self).__init__(*params.get('groups', []))
        self.rect = Rect((0, 0), self.size)
        self.pos = params['pos']

        if 'time_passed' in params:
            self.update(params['time_passed'])

    @property
    def pos(self):
        return self.rect.center

    @pos.setter
    def pos(self, new_pos):
        self.rect.center = new_pos

    def update(self, time):
        self.pos = self.func(self.pos, time)


class HeroineBasicShot(Projectile):
    """Basic heroine's shot

    A glowing blue rectangle moving vertically in bottom-top direction
    """

    @classmethod
    def setup_class_attrs(cls):
        cls.func = movement.linear(angle=90, speed=700)
        cls.image = pygame.image.load(image_path('shot1.png')).convert()
        cls.size = (10, 20)
