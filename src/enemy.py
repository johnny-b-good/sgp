#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame.sprite import DirtySprite

import common
import resource_manager
from helpers import Position


class Enemy(DirtySprite):
    image_id = 'dummy.png'
    health = 16
    pos = Position()
    sprite_groups = (common.enemies_group, common.everything_group)

    def __init__(self, pos=(0, 0), movement=None, attack=None):
        super(Enemy, self).__init__(*self.sprite_groups)
        self.image = resource_manager.images[self.image_id]
        self.rect = self.image.get_rect(center=pos)

        self.life_timer = 0

        self.movement_timer = 0

        if attack:
            # TODO - property naming!
            self.attack = attack
            self.shooting_timer = 0
            self.shooting_counter = 0
            self.attack_delay = attack['from']
            self.shooting_interval = attack['every']
            self.num_of_attacks = attack['times']
            self.attack_type = attack['attack_type']
            self.attack_params = attack['attack_params']

    def _move(self, time):
        self.dirty = 1
        pass

    def _attack(self, time):
        # Can we shoot now?
        self.life_timer += time
        if self.life_timer < self.attack_delay:
            return

        # Tick interval between shots
        self.shooting_timer += time

        # Check shooting conditions - not too fast and not too many
        enough_time_between_shots = self.shooting_timer >= self.shooting_interval
        not_all_attacks_used = self.shooting_counter <= self.num_of_attacks

        if enough_time_between_shots and not_all_attacks_used:
            # Set projectile's spawn position at enemy's coordinates
            self.attack_params['starting_pos'] = self.pos
            # ATTACKING!
            self.attack_type(**self.attack_params)
            # Reset shooting timer
            self.shooting_timer = 0
            # Bump attack counter
            self.shooting_counter += 1

    def update(self, time):
        if self.attack:
            self._attack(time)

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        self.kill()


class Raven(Enemy):
    image_id = 'raven.png'
    health = 32