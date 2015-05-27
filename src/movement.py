import math
import common


def linear(angle=0, speed=100, **kwargs):
    """Build a function describing linear movement

    angle - movement angle in degrees5
    speed - movement speed in pixels per second
    """
    angle_radians = math.radians(angle)
    angle_sin = math.sin(angle_radians)
    angle_cos = math.cos(angle_radians)

    def move(pos=(0, 0), time=0):
        time = float(time) / 1000
        distance = speed * time
        dx = distance * angle_cos
        dy = distance * angle_sin
        x, y = pos
        return x + dx, y - dy

    return move


def aimed(starting_pos, aim_pos, speed=100, **kwargs):
    """ Aimed shot """
    # https://docs.python.org/2/library/math.html#math.atan2
    angle = math.degrees(math.atan2(
        # reversed because of pygame's reverted y axis
        starting_pos[1] - aim_pos[1],
        aim_pos[0] - starting_pos[0]
    ))
    return linear(angle=angle, speed=speed)


def ark():
    pass


def wave():
    pass


def circular():
    pass