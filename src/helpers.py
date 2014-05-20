import os


def image_path(*args):
    """Get image's absolute path"""
    parts = [os.getcwd(), 'gfx'] + list(args)
    return os.path.join(*parts)