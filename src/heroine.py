#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.sprite import Sprite
from pygame.rect import Rect
import math

class Heroine(Sprite):
    UP = (0, -1)
    DOWN = (0, 1)
    LEFT = (-1, 0)
    RIGHT = (1, 0)
    LEFT_UP = (-1, -1)
    RIGHT_UP = (1, -1)
    LEFT_DOWN = (-1, 1)
    RIGHT_DOWN = (1, 1)

    MAX_LIVES = 9
    MAX_BOMBS = 9

    def __init__(self,
                 sprite_size=(50, 50),
                 hitbox_size=(20, 20),
                 speed=10,
                 focus_coefficient=0.5,
                 lives=3,
                 bombs=3,
                 field_ref = None):
        super(Heroine, self).__init__()
        self.rect = Rect((100, 500), sprite_size)
        self.image = pygame.image.load('gfx/reimu.png').convert()
        self.speed = speed
        self._base_speed = speed
        self.focus_coefficient = focus_coefficient
        self.is_focused = False
        self.hitbox = self._create_hitbox(hitbox_size)
        self.lives = lives
        self.bombs = bombs
        self.field_ref = field_ref

    def _create_hitbox(self, hitbox_size):
        """Create heroine's hitbox sprite"""
        hitbox = Sprite()
        hitbox.rect = Rect((0, 0), hitbox_size)
        hitbox.rect.center = self.pos

        hitbox.image = pygame.image.load('gfx/hitbox.png').convert()
        return hitbox

    def move(self, direction):
        """Move heroine on screen"""
        dx, dy = direction
        coefficient = round(1 / math.sqrt(pow(dx, 2) + pow(dy, 2)), 1)
        step_x, step_y = round(dx * coefficient * self.speed), round(dy * coefficient * self.speed)
        current_x, current_y = self.pos
        new_x, new_y = current_x + step_x, current_y + step_y
        self.pos = self._prevent_boundary_collision(new_x, new_y)

    def _prevent_boundary_collision(self, x, y):
        """Check field boundary collision"""
        if x < self.hitbox.rect.width / 2:
            x = self.hitbox.rect.width / 2

        if y < self.hitbox.rect.height / 2:
            y = self.hitbox.rect.height / 2

        if x > self.field_ref.rect.width - self.hitbox.rect.width / 2:
            x = self.field_ref.rect.width - self.hitbox.rect.width / 2

        if y > self.field_ref.rect.height - self.hitbox.rect.height / 2:
            y = self.field_ref.rect.height - self.hitbox.rect.height / 2

        return x, y

    def bonus(self, bonus_type, value):
        pass

    def focus(self, is_focused):
        # TODO: Тестировать кейс, когда focus(True) вызывается многократно
        if is_focused:
            self.speed = self._base_speed * self.focus_coefficient
            self.is_focused = True
        else:
            self.speed = self._base_speed
            self.is_focused = False

    def hit(self):
        if self.lives > 0:
            self.lives -= 1

    def update(self):
        pass



    @property
    def pos(self):
        """Heroine's position on screen"""
        return self.rect.center

    @pos.setter
    def pos(self, new_pos):
        self.rect.center = new_pos
        self.hitbox.rect.center = new_pos