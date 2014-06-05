import movement


def single(projectile_type, starting_pos, movement_type, movement_params, groups=[]):
    """Single bullet attack pattern"""

    projectile_type(pos=starting_pos, func=movement_type(**movement_params), groups=groups)


# def shotgun(projectile_type, starting_pos, speed=100, angle=0, aim_pos=None, spread_angle=30, projectile_num=5):
#     pass
#
#
# def flak(projectile_type, starting_pos, speed=100, angle=0, aim_pos=None):
#     pass
#
#
# def radial(projectile_type, starting_pos, speed=100, angle=0, aim_pos=None):
#     pass