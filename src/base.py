#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *

from heroine import Heroine
from helpers import *


pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.key.set_repeat(0, 10)
FPS = 60
clock = pygame.time.Clock()

playfield = pygame.sprite.Sprite()
playfield.rect = Rect(0, 0, 800, 600)
shots_group = pygame.sprite.Group()
params = {
    'pos': (100, 500),
    'sprite_size': (50, 50),
    'hitbox_size': (20, 20),
    'sprite_image': image_path('reimu.png'),
    'hitbox_image': image_path('hitbox.png'),
    'speed': 400,
    'focus_coefficient': 0.5,
    'lives': 3,
    'bombs': 3,

    'playfield': playfield,
    'heroine_shots_groups': [shots_group],
}

reimu = Heroine(params)
heroine_group = pygame.sprite.Group(reimu)
hitbox_group = pygame.sprite.Group(reimu.hitbox)

time = 0

while True:
    DISPLAYSURF.fill(Color(0, 193, 255))
    heroine_group.draw(DISPLAYSURF)
    shots_group.draw(DISPLAYSURF)

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Focus
    mod_keys = pygame.key.get_mods()
    if mod_keys & KMOD_SHIFT:
        reimu.focus(True)
        hitbox_group.draw(DISPLAYSURF)
    else:
        reimu.focus(False)

    # Directions
    keys = pygame.key.get_pressed()
    if keys[K_LEFT] and keys[K_UP]:
        reimu.move(reimu.LEFT_UP, time)
    elif keys[K_LEFT] and keys[K_DOWN]:
        reimu.move(reimu.LEFT_DOWN, time)
    elif keys[K_RIGHT] and keys[K_UP]:
        reimu.move(reimu.RIGHT_UP, time)
    elif keys[K_RIGHT] and keys[K_DOWN]:
        reimu.move(reimu.RIGHT_DOWN, time)
    elif keys[K_UP]:
        reimu.move(reimu.UP, time)
    elif keys[K_DOWN]:
        reimu.move(reimu.DOWN, time)
    elif keys[K_LEFT]:
        reimu.move(reimu.LEFT, time)
    elif keys[K_RIGHT]:
        reimu.move(reimu.RIGHT, time)
    else:
        pass

    # Shoot the bullet, lol
    if keys[K_x]:
        reimu.shoot(time)

    shots_group.update(time)

    pygame.display.flip()

    time = clock.tick(FPS)