import math


def linear(angle=0, speed=100):
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
        dx = round(distance * angle_cos)
        dy = round(distance * angle_sin)
        x, y = pos
        return x + dx, y - dy

    return move


def aimed(self, aim_pos=0, speed=100):
    angle = int(math.atan(
        (self.pos[0] - aim_pos.pos[0]) /
        (self.pos[1] - aim_pos.pos[1])
    ))
    return linear(angle=angle, speed=speed)


def ark():
    pass


def wave():
    pass


def circular():
    pass