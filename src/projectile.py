#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import DirtySprite
import resource_manager
import movement
import common
from helpers import Position


class Projectile(DirtySprite):
    """Abstract projectile class

    Normally you should not use it , make a subclass, will ya?
    """
    damage = 1
    image_id = 'pellet_pink.png'
    default_func = None
    sprite_groups = [common.enemy_shots_group, common.all_shots_group, common.everything_group]
    pos = Position()

    @classmethod
    def setup_class_attrs(cls, image_id, damage):
        """Setup class attributes"""
        cls.image_id = image_id
        cls.damage = damage

    def __init__(self, pos=(0, 0), func=None):
        super(Projectile, self).__init__(*self.sprite_groups)
        self.image = resource_manager.images[self.image_id]
        self.rect = self.image.get_rect(center=pos)

        if func:
            self.func = func
        elif self.default_func:
            # __func__ is needed to unbind default_func from instance
            # https://docs.python.org/2/reference/datamodel.html
            self.func = self.default_func.__func__

    def update(self, time):
        self.dirty = 1
        self.pos = self.func(self.pos, time)


class HeroineBasicShot(Projectile):
    """Basic heroine's shot - A glowing blue rectangle"""
    damage = 1
    image_id = 'shot3.png'
    default_func = movement.linear(angle=90, speed=1000)
    sprite_groups = [common.heroine_shots_group, common.all_shots_group, common.everything_group]


class RedPellet(Projectile):
    image_id = 'pellet_red.png'


class WhitePellet(Projectile):
    image_id = 'pellet_white.png'