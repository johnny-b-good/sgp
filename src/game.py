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
        # TODO - NO MAGIC ALLOWED
        self.screen = pygame.display.set_mode((1280, 720))
        resource_manager.init()
        pygame.key.set_repeat(0, 10)
        self.clock = pygame.time.Clock()
        self.fps = 60
        self.total_time = 0

        self.playfield_scrolling_interval = 100
        self.playfield_scrolling_timer = 0
        self.playfield_scrolling_speed = 1  # pixels per interval
        self.playfield_vertical_shift = 0

        # Load playfield image, blit it to the screen and update
        self.playfield_surface = resource_manager.images['field.png']
        # TODO - NO MAGIC ALLOWED
        self.screen.blit(self.playfield_surface, Rect(0, 0, 720, 720))
        pygame.display.flip()

        # Create inner and outer playfield boundaries
        # TODO - NO MAGIC ALLOWED
        self.playfield_boundary, self.playfield_outer_boundary = self._create_boundaries(100)
        common.playfield_boundary = self.playfield_boundary

        # Create heroine
        common.heroine = self.heroine = Daria()

        # Load first scenario
        self.load_scenario('scenario1')

        # Launch main loop
        time = 0
        while True:
            # User input
            self.handle_events()
            self.handle_user_input(time)

            # Play next scenario step(s) - create new sprites
            self.play_scenario()

            # Update states of sprites
            self.handle_collisions()
            common.everything_group.update(time)

            # Repaint screen with updated visible sprites
            self.scroll_playfield(time)
            common.everything_group.clear(self.screen, self.playfield_surface)
            updated = common.everything_group.draw(self.screen)
            pygame.display.update(updated)

            # Advance time
            time = self.clock.tick(self.fps)
            self.total_time += time

    def _create_boundaries(self, thickness):
        """ Create inner and outer playfield boundaries """
        # TODO - disconnect calculations from surface
        # TODO - don't "draw" sprites outside inner boundary?
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
        """ Create enemies using parameters from scenario """
        # TODO - optimize this - remove enumerate?
        for index, (time, (enemy_type, enemy_params)) in enumerate(self.scenario):
            if time <= self.total_time:
                enemy_type(**enemy_params)
                self.scenario.pop(index)
            else:
                break

    def scroll_playfield(self, time):
        """ Scroll playfield to imitate flight """
        self.playfield_scrolling_timer += time
        if self.playfield_scrolling_timer >= self.playfield_scrolling_interval:
            # print 'tick', self.playfield_vertical_shift
            # TODO - No magic allowed
            # TODO - Playfield class
            new_playfield = pygame.Surface((720, 720))
            self.playfield_vertical_shift += self.playfield_scrolling_speed
            new_playfield.blit(
                resource_manager.images['field.png'],
                (0, self.playfield_vertical_shift),
            )
            self.playfield_surface = new_playfield

            self.screen.blit(self.playfield_surface, Rect(0, 0, 720, 720))
            pygame.display.flip()

            self.playfield_scrolling_timer = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

    def handle_user_input(self, time):
        # TODO - set only states here, move attacks and movement to Heroine's update method?
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
        # TODO Move to separate game logic module?
        # TODO Change actions to states?
        # Remove heroine's and enemy's shots that left the field
        for sprite in common.all_shots_group:
            if not self.playfield_outer_boundary.contains(sprite.rect):
                sprite.kill()

            if not self.playfield_boundary.contains(sprite.rect):
                sprite.visible = 0
                sprite.dirty = 0
            else:
                sprite.visible = 1
                sprite.dirty = 1





        # Heroine is hit by enemy projectile or enemy itself
        pygame.sprite.spritecollide(self.heroine.hitbox, common.enemy_shots_group, True)
        pygame.sprite.spritecollide(self.heroine.hitbox, common.enemies_group, True)

        # Destroy enemies with heroine's shots
        all_hits = pygame.sprite.groupcollide(common.enemies_group, common.heroine_shots_group, False, True)
        for enemy, projectiles in all_hits.items():
            total_damage = sum(map(lambda p: p.damage, projectiles))
            enemy.hit(total_damage)
