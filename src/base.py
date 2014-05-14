#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import pygame
from pygame.locals import *

from heroine import Heroine

pygame.init()
DISPLAYSURF = pygame.display.set_mode((800, 600))
pygame.key.set_repeat(0, 10)
FPS = 60
clock = pygame.time.Clock()

field = pygame.sprite.Sprite()
field.rect = Rect(0, 0, 800, 600)
reimu = Heroine(field_ref=field, speed=10)
heroine_group = pygame.sprite.Group(reimu)
hitbox_group = pygame.sprite.Group(reimu.hitbox)


while True:
    DISPLAYSURF.fill(Color(0, 193, 255))
    heroine_group.draw(DISPLAYSURF)


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
        reimu.move(reimu.LEFT_UP)
    elif keys[K_LEFT] and keys[K_DOWN]:
        reimu.move(reimu.LEFT_DOWN)
    elif keys[K_RIGHT] and keys[K_UP]:
        reimu.move(reimu.RIGHT_UP)
    elif keys[K_RIGHT] and keys[K_DOWN]:
        reimu.move(reimu.RIGHT_DOWN)
    elif keys[K_UP]:
        reimu.move(reimu.UP)
    elif keys[K_DOWN]:
        reimu.move(reimu.DOWN)
    elif keys[K_LEFT]:
        reimu.move(reimu.LEFT)
    elif keys[K_RIGHT]:
        reimu.move(reimu.RIGHT)
    else:
        pass


        # elif event.type == KEYDOWN and event.key == K_UP:
        #     reimu.move(reimu.UP)
        # elif event.type == KEYDOWN and event.key == K_DOWN:
        #     reimu.move(reimu.DOWN)
        # elif event.type == KEYDOWN and event.key == K_LEFT:
        #     reimu.move(reimu.LEFT)
        # elif event.type == KEYDOWN and event.key == K_RIGHT:
        #     reimu.move(reimu.RIGHT)
        #
        # elif event.type == KEYDOWN and event.key == K_LEFT and event.key == K_UP:
        #     reimu.move(reimu.LEFT_UP)
        # elif event.type == KEYDOWN and event.key == K_LEFT and event.key == K_DOWN:
        #     reimu.move(reimu.LEFT_DOWN)
        # elif event.type == KEYDOWN and event.key == K_RIGHT and event.key == K_UP:
        #     reimu.move(reimu.RIGHT_UP)
        # elif event.type == KEYDOWN and event.key == K_RIGHT and event.key == K_DOWN:
        #     reimu.move(reimu.RIGHT_DOWN)

    pygame.display.flip()

    clock.tick(FPS)