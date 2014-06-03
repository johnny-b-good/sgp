import movement
import math


def simple(enemy, projectile_type, movement_function, groups):
    projectile = projectile_type({
        'pos': enemy.pos,
        'func': movement_function,
        'groups': groups,
    })


def aimed(enemy, projectile_type, speed, groups, heroine):
    """ Shorthand to single aimed shot """
    angle = math.atan((enemy.pos[0] - heroine.pos[0]) / (enemy.pos[1] - heroine.pos[1]))
    movement_function = movement.linear(angle, speed)

    projectile = projectile_type({
        'pos': enemy.pos,
        'func': movement_function,
    })


def radial(enemy, projectile_type, movement_function=movement.linear, projectile_number=0):
    pass


def shotgun(enemy, projectile_type, movement_function=movement.linear, projectile_number=0, spread_angle=30, aimed=False, heroine=None):
    pass


def flak():
    """Concentrated cloud of bullets - how to do this?"""
    pass


def abstract_aimed(self, projectile_type, movement_function, m):
    projectile = projectile_type()
