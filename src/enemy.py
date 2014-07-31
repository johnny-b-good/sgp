#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pygame.sprite import DirtySprite

import common
import resource_manager
from helpers import Position


class Enemy(DirtySprite):
    image_id = 'dummy.png'
    health = 16
    score_bonus = 100
    pos = Position()
    sprite_groups = (common.enemies_group, common.everything_group)

    def __init__(self, pos=(0, 0), movement=None, attack=None):
        super(Enemy, self).__init__(*self.sprite_groups)
        self.image = resource_manager.images[self.image_id]
        self.rect = self.image.get_rect(center=pos)

        self.life_timer = 0

        self.movement_timer = 0

        self.can_attack = False
        if attack:
            self.can_attack = True
            self.attack_timer = 0
            self.attack_counter = 0

            self.attack_delay = attack['from']
            self.attack_interval = attack['every']
            self.attack_num = attack['times']
            self.attack_type = attack['attack_type']
            self.attack_params = attack['attack_params']

        self.can_move = False
        if movement:
            self.can_move = True

    def _move(self, time):
        self.dirty = 1
        pass

    def _attack(self, time):
        # Can we shoot now?
        self.life_timer += time
        if self.life_timer < self.attack_delay:
            return

        # Tick interval between shots
        self.attack_timer += time

        # Check shooting conditions - not too fast and not too many
        enough_time_between_shots = self.attack_timer >= self.attack_interval
        not_all_attacks_used = self.attack_counter <= self.attack_num

        if enough_time_between_shots and not_all_attacks_used:
            # Set projectile's spawn position at enemy's coordinates
            self.attack_params['starting_pos'] = self.pos
            # ATTACKING!
            self.attack_type(**self.attack_params)
            # Reset attack timer
            self.attack_timer = 0
            # Bump attack counter
            self.attack_counter += 1

    def update(self, time):
        if self.can_attack:
            self._attack(time)
        if self.can_move:
            self._move(time)

    def hit(self, damage):
        self.health -= damage
        if self.health <= 0:
            self.die()

    def die(self):
        self.kill()


class Raven(Enemy):
    image_id = 'raven.png'
    health = 32