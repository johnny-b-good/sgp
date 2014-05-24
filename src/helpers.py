import os


def image_path(*args):
    """Get image's absolute path"""
    parts = [os.getcwd(), 'gfx'] + list(args)
    return os.path.join(*parts)


def detect_boundary_leaving(boundary_sprite, projectile_sprite):
    """ Detect if a sprite has left a boundary of another sprite"""
    if projectile_sprite.rect.top < boundary_sprite.rect.top:
        return True
    elif projectile_sprite.rect.left < boundary_sprite.rect.left:
        return True
    elif projectile_sprite.rect.right > boundary_sprite.rect.right:
        return True
    elif projectile_sprite.rect.bottom > boundary_sprite.rect.bottom:
        return True
    else:
        return False