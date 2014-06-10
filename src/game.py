#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import importlib
import pygame
from pygame.locals import *
from pygame.sprite import DirtySprite

from heroine import Daria
from helpers import *
import resource_manager
import common


class Game(object):
    def __init__(self):
        # Initialize basic stuff
        pygame.init()
        # TODO - rename display to screen
        self.display = pygame.display.set_mode((800, 600))
        resource_manager.init()
        pygame.key.set_repeat(0, 10)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.total_time = 0

        # # Create background
        # self.background = Background({
        #     'image': 'background.png',
        #     'size': (800, 600),
        #     'groups': [common.everything_group],
        # })
        #
        # # Create playfield
        # common.playfield = self.playfield = Field({
        #     'size': (600, 600),
        #     'image': 'field.png',
        #     'groups': [common.everything_group],
        #     'boundary_thickness': 300
        # })

        # TODO - document me
        self.playfield_surface = resource_manager.images['field.png']
        self.display.blit(self.playfield_surface, Rect(0, 0, 600, 600))
        pygame.display.flip()  # TODO - Gotta flip to update screen

        common.playfield = self.playfield_boundary = self.playfield_surface.get_rect()

        self.boundary_thickness = 300  # TODO - NO MAGIC ALLOWED
        self.playfield_outer_boundary = Rect(
            -self.boundary_thickness, -self.boundary_thickness,
            self.playfield_boundary.width + 2 * self.boundary_thickness,
            self.playfield_boundary.height + 2 * self.boundary_thickness
        )




        # Create heroine
        common.heroine = self.heroine = Daria()

        # Load first scenario
        self.load_scenario('scenario1')

        # Launch main loop
        time = 0
        while True:
            # Clean screen with background
            common.everything_group.clear(self.display, self.playfield_surface)

            self.handle_events()
            self.handle_user_input(time)
            self.play_scenario()
            self.handle_collisions()
            common.everything_group.update(time)

            updated = common.everything_group.draw(self.display)
            pygame.display.update(updated)

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
        # TODO - create common group for shots
        # TODO - remove boundary from helpers
        for sprite in common.heroine_shots_group:
            if not self.playfield_outer_boundary.contains(sprite.rect):
                sprite.kill()

        # TODO - restore this shit
        # pygame.sprite.spritecollide(self.playfield.boundary, common.heroine_shots_group, True, detect_boundary_leaving)
        # pygame.sprite.spritecollide(self.playfield.boundary, common.enemy_shots_group, True, detect_boundary_leaving)

        # Heroine is hit by enemy projectile or enemy itself
        pygame.sprite.spritecollide(self.heroine, common.enemy_shots_group, True)
        pygame.sprite.spritecollide(self.heroine, common.enemies_group, True)

        # Destroy enemies with heroine's shots
        damaged_enemies = pygame.sprite.groupcollide(common.enemies_group, common.heroine_shots_group, False, True)
        for enemy, projectiles in damaged_enemies.items():
            total_damage = sum(map(lambda p: p.damage, projectiles))
            enemy.hit(total_damage)



# # TODO field and background convert to surfaces?
# class Field(DirtySprite):
#     def __init__(self, params):
#         super(Field, self).__init__(*params.get('groups', []))
#         self.rect = Rect((0, 0), params['size'])
#         self.image = resource_manager.images[params['image']]
#         self.boundary = DirtySprite()
#         self.boundary_thickness = params['boundary_thickness']
#         self.boundary.rect = Rect(
#             -self.boundary_thickness, -self.boundary_thickness,
#             self.rect.width + 2 * self.boundary_thickness,
#             self.rect.height + 2 * self.boundary_thickness
#         )
#
#
# class Background(DirtySprite):
#     def __init__(self, params):
#         super(Background, self).__init__(*params.get('groups', []))
#         self.rect = Rect((0, 0), params['size'])
#         self.image = resource_manager.images[params['image']]
