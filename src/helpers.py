def detect_boundary_leaving(boundary_sprite, projectile_sprite):
    """ Detect if a sprite has left a boundary of another sprite"""
    return not boundary_sprite.rect.contains(projectile_sprite)