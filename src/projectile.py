#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import DirtySprite
import resource_manager
import movement
import common


class Projectile(DirtySprite):
    """Abstract projectile class

    Normally you should not use it , make a subclass, will ya?
    """
    damage = 0
    image_id = 'pellet_pink.png'
    default_func = None
    groups = [common.enemy_shots_group, common.everything_group]

    @classmethod
    def setup_class_attrs(cls, image_id, damage):
        """Setup class attributes"""
        cls.image_id = image_id
        cls.damage = damage

    def __init__(self, pos=(0, 0), func=None):
        super(Projectile, self).__init__(*self.groups)
        self.image = resource_manager.images[self.image_id]
        self.rect = self.image.get_rect(center=pos)

        if func:
            self.func = func
        elif self.default_func:
            # __func__ is needed to unbind default_func from instance
            # https://docs.python.org/2/reference/datamodel.html
            self.func = self.default_func.__func__

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
    damage = 1
    image_id = 'shot2.png'
    default_func = movement.linear(angle=90, speed=700)
    groups = [common.heroine_shots_group, common.everything_group]
