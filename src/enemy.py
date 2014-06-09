#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame.sprite import DirtySprite

import resource_manager
import attack
import movement
import common


class Enemy(DirtySprite):
    image_id = 'enemy.png'
    health = 100

    def __init__(self, pos, moving=[], attacking=[]):
        super(Enemy, self).__init__(common.enemies_group, common.everything_group)
        self.image = resource_manager.images[self.image_id]
        self.rect = self.image.get_rect(center=pos)

        self._movement_timer = 0
        self._shooting_timer = 0
        self.movement = movement
        self.attack = attack

    @property
    def pos(self):
        return self.rect.center

    @pos.setter
    def pos(self, new_pos):
        self.rect.center = new_pos

    def _move(self, time):
        pass

    def _attack(self, time):
        pass

    def update(self, time):
        pass

    def hit(self, damage):
        pass