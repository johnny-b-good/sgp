#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import DirtySprite
import resource_manager
import movement


class Projectile(DirtySprite):
    """Abstract projectile class

    You should not use it normally, make a subclass, will ya?
    """

    @classmethod
    def setup_class_attrs(cls, image_id, damage):
        """Setup class attributes"""
        cls.image_id = image_id
        cls.damage = damage

    def __init__(self, pos=(0, 0), groups=[], func=None):
        super(Projectile, self).__init__(*groups)
        self.image = resource_manager.images[self.image_id]
        self.rect = self.image.get_rect(center=pos)
        self.func = func
        # TODO func cached in da class?

    @property
    def pos(self):
        return self.rect.center

    @pos.setter
    def pos(self, new_pos):
        self.rect.center = new_pos

    def update(self, time):
        self.pos = self.func(self.pos, time)


class HeroineBasicShot(Projectile):
    """Basic heroine's shot - A glowing blue rectangle"""
    # func = movement.linear(angle=45, speed=700)
    image_id = 'shot2.png'
    damage = 10
