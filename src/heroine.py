#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import pygame
from pygame.sprite import DirtySprite
from pygame.surface import Surface

import resource_manager
from projectile import *
import attack
import movement
import common


class Heroine(DirtySprite):
    RIGHT = 0
    RIGHT_UP = 45
    UP = 90
    LEFT_UP = 135
    LEFT = 180
    LEFT_DOWN = 225
    DOWN = 270
    RIGHT_DOWN = 315

    MAX_LIVES = 9
    MAX_BOMBS = 9

    sprite_groups = [common.everything_group]
    pos = Position(callback='_on_pos_update')

    def __init__(self, pos, image_id, lives, bombs,
                 base_speed, focus_mod, hitbox):
        super(Heroine, self).__init__(*self.sprite_groups)
        # Load sprite's image
        self.image = resource_manager.images[image_id]
        # Sprite's rect
        self.rect = self.image.get_rect(center=pos)
        # Create hitbox sprite
        hitbox['pos'] = self.pos
        self.hitbox = Hitbox(**hitbox)
        # Heroine's current speed
        self.speed = base_speed
        # Heroine's base speed
        self.base_speed = base_speed
        # Focus coefficient defines how speed changes in the focused mode
        self.focus_mod = focus_mod
        # Is heroine focused
        self.is_focused = False
        # # Number of lives
        self.lives = lives
        # # Number of bombs
        self.bombs = bombs
        # Reference to playfield object
        self.playfield = common.playfield_boundary
        # TODO: DOCUMENT ME
        self.shot_timer = 0

    def _on_pos_update(self):
        """ Callback on heroine's movement

        Update hitbox position and set dirty flags for heroine and her hitbox
        """
        self.dirty = 1
        self.hitbox.pos = self.pos
        self.hitbox.dirty = 1

    def move(self, angle, time):
        """Move heroine on screen"""
        # TODO Кешировать функции для всех направлений и двух скоростей?5
        time = float(time) / 1000
        distance = time * self.speed
        angle_radians = math.radians(angle)
        dx = round(distance * math.cos(angle_radians))
        dy = round(distance * math.sin(angle_radians))
        current_x, current_y = self.pos
        new_x, new_y = current_x + dx, current_y - dy
        self.pos = self._prevent_boundary_collision(new_x, new_y)

    def _prevent_boundary_collision(self, x, y):
        """Check field boundary collision"""
        # TODO - remove repetitions
        # if self.hitbox.rect.bottom > self.playfield.bottom:
        #     self.hitbox.rect.bottom = self.playfield.bottom
        # elif self.hitbox.rect.top < self.playfield.top:
        #     self.hitbox.rect.top = self.playfield.top
        #
        # if self.hitbox.rect.left < self.playfield.left:
        #     self.hitbox.rect.left = self.playfield.left
        # elif self.hitbox.rect.right > self.playfield.right:
        #     self.hitbox.rect.right = self.playfield.right

        if x < self.hitbox.rect.width / 2:
            x = self.hitbox.rect.width / 2

        if y < self.hitbox.rect.height / 2:
            y = self.hitbox.rect.height / 2

        if x > self.playfield.width - self.hitbox.rect.width / 2:
            x = self.playfield.width - self.hitbox.rect.width / 2

        if y > self.playfield.height - self.hitbox.rect.height / 2:
            y = self.playfield.height - self.hitbox.rect.height / 2

        return x, y

    def bonus(self, bonus_type, value):
        pass

    def focus(self, is_focused):
        """Set/unset focused mode"""
        # TODO: Тестировать кейс, когда focus(True) вызывается многократно
        if is_focused:
            self.speed = self.base_speed * self.focus_mod
            self.is_focused = True
            self.hitbox.is_focused = True
        else:
            self.speed = self.base_speed
            self.is_focused = False
            self.hitbox.is_focused = False

    def hit(self):
        if self.lives > 0:
            self.lives -= 1

    def update(self, *args):
        """Sprite animation goes here"""
        pass

    def shoot(self, time):
        """Generic heroine shooting method

        Should be replaced in  subclasses"""
        # TODO: POWERLEVEL!
        # TODO: Shot spawn spots
        # TODO Move shooting interval to self

        # five shots per second
        shooting_interval = 50
        self.shot_timer += time

        if self.shot_timer >= shooting_interval:
            attack.single(
                projectile_type=HeroineBasicShot,
                starting_pos=self.pos,
            )
            self.shot_timer = 0

    def bomb(self, time):
        pass


class Hitbox(DirtySprite):
    sprite_groups = [common.everything_group]
    pos = Position()

    """ Heroine's hitbox sprite """
    def __init__(self, pos, image_id):
        super(Hitbox, self).__init__(*self.sprite_groups)
        # Load hitbox's image
        self._image = resource_manager.images[image_id]
        # Create hitbox's rectangle and set it's position
        self.rect = self._image.get_rect(center=pos)
        # Empty image for unfocused mode
        self._null_image = Surface((0, 0))
        # Is heroine focused?
        self.is_focused = False

    @property
    def image(self):
        if self.is_focused:
            return self._image
        else:
            return self._null_image


class Daria(Heroine):
    """ First heroine - Daria """
    def __init__(self):
        super(Daria, self).__init__(
            pos=(300, 500),
            image_id='daria4.png',
            lives=3,
            bombs=3,
            base_speed=300,
            focus_mod=0.5,
            hitbox={'image_id': 'hitbox3.png'}
        )
