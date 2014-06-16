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
        self.screen = pygame.display.set_mode((1280, 720))
        resource_manager.init()
        pygame.key.set_repeat(0, 10)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.total_time = 0

        # Load playfield image, blit it to the screen and update
        self.playfield_surface = resource_manager.images['field.png']
        self.screen.blit(self.playfield_surface, Rect(0, 0, 720, 720))
        pygame.display.flip()

        # Create inner and outer playfield boundaries
        # TODO - NO MAGIC ALLOWED
        self.playfield_boundary, self.playfield_outer_boundary = self._create_boundaries(300)
        common.playfield_boundary = self.playfield_boundary

        # Create heroine
        common.heroine = self.heroine = Daria()

        # Load first scenario
        self.load_scenario('scenario1')

        # Launch main loop
        time = 0
        while True:
            # Clean screen of sprites with background
            common.everything_group.clear(self.screen, self.playfield_surface)

            # TODO - document those
            self.handle_events()
            self.handle_user_input(time)
            self.play_scenario()
            self.handle_collisions()
            common.everything_group.update(time)

            # Repaint screen with updated sprites
            updated = common.everything_group.draw(self.screen)
            pygame.display.update(updated)

            # Advance time
            time = self.clock.tick(self.fps)
            self.total_time += time

    def _create_boundaries(self, thickness):
        """ Create inner and outer playfield boundaries """
        inner_boundary = self.playfield_surface.get_rect()
        outer_boundary = Rect(
            -thickness, -thickness,
            inner_boundary.width + 2 * thickness,
            inner_boundary.height + 2 * thickness
        )
        return inner_boundary, outer_boundary

    def load_scenario(self, scenario_name):
        """ Load scenario steps from module """
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

        # Exit game with the Esc button
        if keys[K_ESCAPE]:
            pygame.quit()
            sys.exit()

    def handle_collisions(self):
        # Remove heroine's and enemy's shots that left the field
        for sprite in common.all_shots_group:
            if not self.playfield_outer_boundary.contains(sprite.rect):
                sprite.kill()

        # Heroine is hit by enemy projectile or enemy itself
        pygame.sprite.spritecollide(self.heroine, common.enemy_shots_group, True)
        pygame.sprite.spritecollide(self.heroine, common.enemies_group, True)

        # Destroy enemies with heroine's shots
        all_hits = pygame.sprite.groupcollide(common.enemies_group, common.heroine_shots_group, False, True)
        for enemy, projectiles in all_hits.items():
            total_damage = sum(map(lambda p: p.damage, projectiles))
            enemy.hit(total_damage)
