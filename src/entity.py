#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
from collections import namedtuple
import pygame
from pygame.sprite import DirtySprite
# from pygame.surface import Surface

# import resource_manager
# import common

class Entity(DirtySprite):
    """Any game object"""
    
    def __init__(self):
        super(Entity, self).__init__()
        self.rect = Rect()
        self._pos = (0.0, 0.0)

    @property
    def pos(self):
        return self._pos

    @pos.setter
    def pos(self, new_value):
        self._pos = new_value
        self.rect.center = (math.floor(new_value[0]), math.floor(new_value[1]))
        
    def update(self):
        pass
    

class AnimationSequence(object):
    """docstring for AnimationSequence"""
    def __init__(self, sprite):
        super(AnimationSequence, self).__init__()
        self.current_image = None
        self.sheet_image = None
        self.sprite = sprite
        self.current_step = 0
        self.current_time = 0
        # self.step_params = []
        # self.steps = [self.build_step(step) for step in self.step_params]

    def advance(self):
        current_step_is_last = (self.current_step == len(self.steps) - 1)
        if current_step_is_last:
            self.current_step = 0 
        else:
            self.current_step += 1
        
    def build_step(self, params):
        # image = pygame.Surface([width, height]).convert()
        # image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))
        step = {
            'num': None
            'time': None,
            'image': None
        }
        return step
