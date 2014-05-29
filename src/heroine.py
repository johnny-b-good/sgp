#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import pygame
from pygame.sprite import Sprite
from pygame.rect import Rect
from pygame.surface import Surface

import resource_manager
import projectile


class Heroine(Sprite):
    # TODO - hitbox optimize, separate class
    # TODO - hitbox - null image when focused
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

    def __init__(self, params):
        super(Heroine, self).__init__(*params.get('sprite_groups', []))
        # Sprite's rect
        self.rect = Rect((0, 0), params['sprite_size'])
        # Create hitbox sprite
        self.hitbox = Hitbox(params)
        # Set heroine's coordinates
        self.pos = params['pos']
        # Load sprite's image
        self.image = resource_manager.images[params['sprite_image']]
        # Heroine's current speed
        self.speed = params['speed']
        # Heroine's base speed
        self._base_speed = self.speed
        # Focus coefficient defines how speed changes in the focused mode
        self.focus_coefficient = params['focus_coefficient']
        # Is heroine focused
        self.is_focused = False
        # Number of lives
        self.lives = params['lives']
        # Number of bombs
        self.bombs = params['bombs']
        # Reference to playfield object
        self.playfield = params['playfield']
        # Reference to heroine's shots Group
        self.heroine_shots_groups = params['heroine_shots_groups']
        # TODO: DOCUMENT ME
        self.shot_timer = 0

    def move(self, angle, time):
        """Move heroine on screen"""
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

        if x < self.hitbox.rect.width / 2:
            x = self.hitbox.rect.width / 2

        if y < self.hitbox.rect.height / 2:
            y = self.hitbox.rect.height / 2

        if x > self.playfield.rect.width - self.hitbox.rect.width / 2:
            x = self.playfield.rect.width - self.hitbox.rect.width / 2

        if y > self.playfield.rect.height - self.hitbox.rect.height / 2:
            y = self.playfield.rect.height - self.hitbox.rect.height / 2

        return x, y

    def bonus(self, bonus_type, value):
        pass

    def focus(self, is_focused):
        """Set/unset focused mode"""
        # TODO: Тестировать кейс, когда focus(True) вызывается многократно
        if is_focused:
            self.speed = self._base_speed * self.focus_coefficient
            self.is_focused = True
            self.hitbox.is_focused = True
        else:
            self.speed = self._base_speed
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

        # five shots per second
        shooting_interval = 50
        self.shot_timer += time

        if self.shot_timer >= shooting_interval:
            projectile.HeroineBasicShot({
                'groups': self.heroine_shots_groups,
                'pos': self.pos
            })
            self.shot_timer = 0

    def bomb(self, time):
        pass

    @property
    def pos(self):
        """Heroine's position on screen"""
        return self.rect.center

    @pos.setter
    def pos(self, new_pos):
        self.rect.center = new_pos
        self.hitbox.pos = new_pos


class Hitbox(Sprite):
    """ Heroine's hitbox sprite """
    def __init__(self, params):
        super(Hitbox, self).__init__(*params.get('hitbox_groups', []))
        # Create hitbox's rectangle and set it's position
        self.rect = Rect((0, 0), params['hitbox_size'])
        self.rect.center = params['pos']
        # Load hitbox's image
        self._image = resource_manager.images[params['hitbox_image']]
        # Empty image for unfocused mode
        self._null_image = Surface((0, 0))
        # Is heroine focused?
        self.is_focused = False

    def update(self, *args):
        """Sprite animation goes here"""
        pass

    @property
    def image(self):
        if self.is_focused:
            return self._image
        else:
            return self._null_image

    @property
    def pos(self):
        return self.rect.center

    @pos.setter
    def pos(self, new_pos):
        self.rect.center = new_pos


class Reimu(Heroine):
    params = {}

    def __init__(self):
        super(Reimu, self).__init__(params)
