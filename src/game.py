#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import importlib
import pygame
from pygame.locals import *
from pygame.sprite import DirtySprite

from heroine import Heroine
from helpers import *
import resource_manager
import common


class Game(object):
    def __init__(self):
        # Initialize basic stuff
        pygame.init()
        self.display = pygame.display.set_mode((800, 600), FULLSCREEN)
        resource_manager.init()
        pygame.key.set_repeat(0, 10)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.total_time = 0

        # Create background
        self.background = Background({
            'image': 'background.png',
            'size': (800, 600),
            'groups': [common.everything_group],
        })

        # Create playfield
        self.playfield = Field({
            'size': (600, 600),
            'image': 'field.png',
            'groups': [common.everything_group],
            'boundary_thickness': 300
        })

        # Create heroine
        common.heroine = self.heroine = Heroine({
            'pos': (300, 500),

            'sprite_size': (20, 50),
            'sprite_image': 'daria2.png',
            'sprite_groups': [common.everything_group],

            'hitbox_size': (8, 8),
            'hitbox_image': 'hitbox3.png',
            'hitbox_groups': [common.everything_group],

            'lives': 3,
            'bombs': 3,

            'speed': 300,
            'focus_coefficient': 0.5,

            'heroine_shots_groups': [common.heroine_shots_group, common.everything_group],

            'playfield': self.playfield
        })

        # Load first scenario
        self.load_scenario('scenario1')
        print self.scenario

        # Launch main loop
        time = 0
        while True:
            self.handle_events()
            self.handle_user_input(time)
            self.play_scenario()
            self.handle_collisions()
            common.everything_group.update(time)
            common.everything_group.draw(self.display)
            pygame.display.flip()
            time = self.clock.tick(self.fps)
            self.total_time += time

    def load_scenario(self, scenario_name):
        """ Load scenario steps from module """
        # self.scenario = __import__(scenario_name, fromlist=['scenario']).scenario
        self.scenario = importlib.import_module('src.%s' % scenario_name).scenario

    def play_scenario(self):
        # print self.total_time, len(self.scenario)
        for index, (time, step) in enumerate(self.scenario):
            if time <= self.total_time:
                step()
                self.scenario.pop(index)
            else:
                break

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
            # print common.heroine_shots_group, common.everything_group

        # Exit game with the Esc button
        if keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()

    def handle_collisions(self):
        # Remove heroine's and enemy's shots that left the field
        pygame.sprite.spritecollide(self.playfield.boundary, common.heroine_shots_group, True, detect_boundary_leaving)
        pygame.sprite.spritecollide(self.playfield.boundary, common.enemy_shots_group, True, detect_boundary_leaving)

        # Heroine is hit by enemy projectile or enemy itself
        pygame.sprite.spritecollide(self.heroine, common.enemy_shots_group, True)
        pygame.sprite.spritecollide(self.heroine, common.enemies_group, True)

        # Destroy enemies with heroine's shots
        enemy_and_projectiles_collisions = pygame.sprite.groupcollide(common.heroine_shots_group, common.enemies_group, True, False)
        # for dead_people in enemy_and_projectiles_collisions.values():
        #     for enemies in dead_people:
        #         enemy_hit


# TODO field and background convert to surfaces?
class Field(DirtySprite):
    def __init__(self, params):
        super(Field, self).__init__(*params.get('groups', []))
        self.rect = Rect((0, 0), params['size'])
        self.image = resource_manager.images[params['image']]
        self.boundary = DirtySprite()
        self.boundary_thickness = params['boundary_thickness']
        self.boundary.rect = Rect(
            -self.boundary_thickness, -self.boundary_thickness,
            self.rect.width + 2 * self.boundary_thickness, self.rect.height + 2 * self.boundary_thickness)


class Background(DirtySprite):
    def __init__(self, params):
        super(Background, self).__init__(*params.get('groups', []))
        self.rect = Rect((0, 0), params['size'])
        self.image = resource_manager.images[params['image']]
