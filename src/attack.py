import movement


def simple(enemy, projectile_class, movement_function=movement.linear, aimed=False, heroine=None):
    if aimed and heroine:
        pass
    projectile = projectile_class({
        'pos': enemy.pos,
        'func': movement_function,
    })


def aimed(enemy, projectile_class, heroine):
    """ Shorthand to single aimed shot """
    pass


def radial(enemy, projectile_class, movement_function=movement.linear, projectile_number=0):
    pass


def shotgun(enemy, projectile_class, movement_function=movement.linear, projectile_number=0, spread_angle=30, aimed=False, heroine=None):
    pass


def flak():
    """Concentrated cloud of bullets - how to do this?"""
    pass