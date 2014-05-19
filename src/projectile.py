#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite
from pygame.rect import Rect


class Projectile(Sprite):
    def __init__(self, params):
        super(Projectile, self).__init__()
        self.rect = Rect((0, 0), params['size'])
        self.pos = params['pos']
        self.image = pygame.image.load(params['image']).convert()
        self.func = params['func']

    @property
    def pos(self):
        return self.rect.center

    @pos.setter
    def pos(self, new_pos):
        self.rect.center = new_pos

    def update(self, time):
        self.pos = self.func(self.pos, time)
