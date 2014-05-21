#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math
import pygame
from pygame.sprite import Sprite
from pygame.rect import Rect

import projectile


class Heroine(Sprite):
    # TODO - Clear up directions and movement <============== THIS!!!!
    # TODO - Move input events handling here
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
        super(Heroine, self).__init__()
        # Sprite's rect
        self.rect = Rect((0, 0), params['sprite_size'])
        # Create hitbox sprite
        self.hitbox = self._create_hitbox(params['hitbox_size'], params['hitbox_image'])
        # Set heroine's coordinates
        self.pos = params['pos']
        # Load sprite's image
        self.image = pygame.image.load(params['sprite_image']).convert()
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
        self.field_ref = params['field_ref']
        # Reference to heroine's shots Group
        self.shots_group_ref = params['shots_group_ref']
        # Initialize shot classes
        projectile.HeroineBasicShot.setup_class_attrs()
        #
        self.shot_timer = 0

    def _create_hitbox(self, hitbox_size, image):
        """Create heroine's hitbox sprite"""
        hitbox = Sprite()
        hitbox.rect = Rect((0, 0), hitbox_size)
        hitbox.rect.center = self.pos

        hitbox.image = pygame.image.load(image).convert()
        return hitbox

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
        """Set/unset focused mode"""
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
                'groups': [self.shots_group_ref],
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
        self.hitbox.rect.center = new_pos