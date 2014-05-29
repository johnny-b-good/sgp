#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import DirtySprite
from pygame.rect import Rect

import movement
import resource_manager


class Projectile(DirtySprite):
    """Abstract projectile class

    You should not use it normally, make a subclass, will ya?
    """

    @classmethod
    def setup_class_attrs(cls, params):
        """Setup class attributes"""
        cls.func = params['func']
        cls.image_id = params['image_id']
        cls.size = params['size']
        cls.damage = params['damage']

    def __init__(self, params):
        super(Projectile, self).__init__(*params.get('groups', []))
        self.rect = Rect((0, 0), self.size)
        self.image = resource_manager.images[self.image_id]
        self.pos = params['pos']

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

    func = movement.linear(angle=90, speed=700)
    image_id = 'shot1.png'
    size = (10, 20)
