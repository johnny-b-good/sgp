import common
import movement


def single(projectile_type, starting_pos, movement_type=None, movement_params={}):
    """Single bullet attack pattern"""
    movement_params['starting_pos'] = starting_pos
    movement_params['aim_pos'] = common.heroine.pos
    if movement_type:
        projectile_type(pos=starting_pos, func=movement_type(**movement_params))
    else:
        projectile_type(pos=starting_pos)


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