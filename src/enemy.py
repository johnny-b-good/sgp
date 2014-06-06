#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame.sprite import DirtySprite

import resource_manager
import attack


class Enemy(DirtySprite):
    image_id = 'enemy.png'
    health = 1

    def __init__(self, pos, movement, attack, groups=[]):
        super(Enemy, self).__init__(*groups)
        self.image = resource_manager.images[self.image_id]
        self.rect = self.image.get_rect(center=pos)

        self.heroine = params['heroine']
        self.enemy_shots_group = params['enemy_shots_groups']

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

