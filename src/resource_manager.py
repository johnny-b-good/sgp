#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import pygame

# Resource directories
IMAGES_DIR = 'gfx'
SOUNDS_DIR = 'snd'

# Resource storage dicts
images = {}
sounds = {}


def init():
    """ Load resources to storages

    This should be called explicitly
    due to pygame-cannot-convert-image-without-initialized-display bullshit
    """
    global images, sounds
    images = _load_images()
    sounds = _load_sounds()


def _create_file_id(name):
    """ Create file id as nix-style path without root resource folder """
    path_list = name.split(os.sep)
    path_list.pop(0)
    return '/'.join(path_list)


def _check_file_extention(filename, extentions):
    """ Check if file has extention that's defined in extentions list """
    name, ext = os.path.splitext(filename)
    return ext in extentions


def _get_files_dict(root, extentions=[]):
    """ Create a dict of file_id:file_path pairs from a list of file_paths"""
    names = []
    for current_dir, dirs, files in os.walk(root):
        files = filter(lambda f: _check_file_extention(f, extentions), files)
        names += map(lambda f: os.path.join(current_dir, f), files)

    return dict((_create_file_id(name), name) for name in names)


def _load_images():
    """ Recursivly load all images from directory """
    files_dict = _get_files_dict(IMAGES_DIR, ['.png'])

    for file_id, file_path in files_dict.iteritems():
        try:
            image = pygame.image.load(file_path)
        except pygame.error:
            raise IOError('Cannot load image: %s' % file_path)

        image = image.convert_alpha()

        # TODO - do we really need this shit?
        # if colorkey is not None:
        #     if colorkey is -1:
        #         colorkey = image.get_at((0,0))
        #     image.set_colorkey(colorkey, RLEACCEL)

        files_dict[file_id] = image

    return files_dict


def _load_sounds():
    """ Recursivly load all sounds from directory """
    return {}


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_mode((100, 100))

    init()
    print images, sounds