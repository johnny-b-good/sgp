#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *
from pygame.sprite import Group


class Game(object):
    def __init__(self):
        # Initialize basic stuff
        pygame.init()
        self.display = pygame.display.set_mode((800, 600))
        pygame.key.set_repeat(0, 10)
        self.clock = pygame.time.Clock()
        self.fps = 60

        # Create sprite groups
        self.everything_group = Group()
        self.heroine_shots_group = Group()
        self.enemies_group = Group()
        self.enemy_shots_group = Group()
        self.explosions_group = Group(5)
        self.bonuses_group = Group()
        self.indicators_group = Group()

        # Create heroine
        self.heroine = None

        # Create playfield
        self.field = None

        # Create background
        self.background = None

        # Launch main loop
        time = 0
        while True:
            self.main_loop(time)
            time = self.clock.tick(self.fps)

    def main_loop(self, time):
        self.handle_user_input(time)
        self.handle_collisions()
        self.everything_group.update(time)
        self.everything_group.draw()
        pygame.display.flip()

    def load_scenarios(self):
        pass

    def handle_collisions(self):
        pass

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

i