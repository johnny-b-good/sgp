#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import pygame
from pygame.sprite import DirtySprite
from pygame.rect import Rect

import resource_manager
import attack


class Enemy(DirtySprite):
    def __init__(self, params):
        super(Enemy, self).__init__(*params.get('sprite_groups', []))
        self.rect = Rect((0, 0), params['sprite_size'])
        self.pos = params['pos']
        self.image = resource_manager.images[params['sprite_image']]
        self.health = params['health']

        self.enemy_shots_group = params['enemy_shots_groups']

        self._movement_timer = 0
        self._shooting_timer = 0
        self.movement_scenario = params['movement_scenario']
        self.shooting_scenario = params['shooting_scenario']

    @property
    def pos(self):
        return self.rect.center

    @pos.setter
    def pos(self, new_pos):
        self.rect.center = new_pos

    def _move(self, time):
        pass

    def _shoot(self, time):
        pass

    def update(self, time):
        pass

