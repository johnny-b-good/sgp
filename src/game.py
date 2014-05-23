#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *
from pygame.sprite import Sprite, Group, OrderedUpdates
from pygame.surface import Surface

from heroine import Heroine
from helpers import *


class Game(object):
    def __init__(self):
        # Initialize basic stuff
        pygame.init()
        self.display = pygame.display.set_mode((800, 600))
        pygame.key.set_repeat(0, 10)
        self.clock = pygame.time.Clock()
        self.fps = 60

        # Create sprite groups
        self.everything_group = OrderedUpdates()
        self.heroine_shots_group = Group()
        self.enemies_group = Group()
        self.enemy_shots_group = Group()
        self.explosions_group = Group()
        self.bonuses_group = Group()
        self.indicators_group = Group()
        self.boundaries_group = Group()

        # Create background
        self.background = Background({
            'image': image_path('background.png'),
            'size': (800, 500),
            'groups': [self.everything_group],
        })

        # Create playfield
        self.playfield = Field({
            'size': (600, 600),
            'groups': [self.everything_group],
            'boundaries_group': self.boundaries_group
        })

        # Create heroine
        self.heroine = Heroine({
            'pos': (400, 500),

            'sprite_size': (50, 50),
            'sprite_image': image_path('reimu.png'),
            'sprite_groups': [self.everything_group],

            'hitbox_size': (20, 20),
            'hitbox_image': image_path('hitbox.png'),
            'hitbox_groups': [self.everything_group],

            'lives': 3,
            'bombs': 3,

            'speed': 400,
            'focus_coefficient': 0.5,

            'heroine_shots_groups': [self.heroine_shots_group, self.everything_group],

            'playfield': self.playfield
        })

        # Launch main loop
        time = 0
        while True:
            self.handle_events()
            self.handle_user_input(time)
            self.handle_collisions()
            self.everything_group.update(time)
            self.display.fill((0, 193, 255))
            self.everything_group.draw(self.display)
            pygame.display.flip()
            time = self.clock.tick(self.fps)

    def load_scenarios(self):
        pass

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def handle_user_input(self, time):
        # Focus
        mod_keys = pygame.key.get_mods()
        if mod_keys & KMOD_SHIFT:
            self.heroine.focus(True)
        else:
            self.heroine.focus(False)

        # Directions
        keys = pygame.key.get_pressed()
        if keys[K_LEFT] and keys[K_UP]:
            self.heroine.move(self.heroine.LEFT_UP, time)
        elif keys[K_LEFT] and keys[K_DOWN]:
            self.heroine.move(self.heroine.LEFT_DOWN, time)
        elif keys[K_RIGHT] and keys[K_UP]:
            self.heroine.move(self.heroine.RIGHT_UP, time)
        elif keys[K_RIGHT] and keys[K_DOWN]:
            self.heroine.move(self.heroine.RIGHT_DOWN, time)
        elif keys[K_UP]:
            self.heroine.move(self.heroine.UP, time)
        elif keys[K_DOWN]:
            self.heroine.move(self.heroine.DOWN, time)
        elif keys[K_LEFT]:
            self.heroine.move(self.heroine.LEFT, time)
        elif keys[K_RIGHT]:
            self.heroine.move(self.heroine.RIGHT, time)
        else:
            pass

        # Shoot the bullet, lol
        if keys[K_x]:
            self.heroine.shoot(time)
            print self.heroine_shots_group, self.everything_group

    def handle_collisions(self):
        # pygame.sprite.groupcollide(self.heroine_shots_group, self.boundaries_group, True, False)
        pass


class Field(Sprite):
    def __init__(self, params):
        super(Field, self).__init__(*params.get('groups', []))
        self.rect = Rect((0, 0), params['size'])
        # self.image = Surface(params['size']).fill(Color(0, 193, 255))
        self.image = Surface(params['size'])
        self.image.fill(Color(0, 193, 255))
        # width = self.rect.width + 200
        boundary_thickness = 100
        boundary_margin = 100
        boundary_width = self.rect.width + 2 * boundary_margin
        boundary_height = self.rect.height + 2 * boundary_margin
        self.boundary_sizes = {
            'top': Rect(-boundary_margin, -boundary_margin-boundary_thickness, boundary_width, boundary_thickness),
            'right': Rect(boundary_width, -boundary_margin, boundary_thickness, boundary_height),
            'bottom': Rect(-boundary_margin, boundary_height, boundary_width, boundary_thickness),
            'left': Rect(-boundary_margin - boundary_thickness, -boundary_margin, boundary_thickness, boundary_height),
        }
        for boundary_rect in self.boundary_sizes.values():
            boundary = Sprite(params['boundaries_group'])
            boundary.rect = boundary_rect


class Background(Sprite):
    def __init__(self, params):
        super(Background, self).__init__(*params.get('groups', []))
        self.rect = Rect((0, 0), params['size'])
        self.image = pygame.image.load(params['image']).convert()



if __name__ == '__main__':
    Game()