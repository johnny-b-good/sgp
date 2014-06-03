import math


def linear(angle=0, speed=100):
    """Build a function describing linear movement

    angle - movement angle in degrees5
    speed - movement speed in pixels per second
    """
    angle_radians = math.radians(angle)
    angle_sin = math.sin(angle_radians)
    angle_cos = math.cos(angle_radians)

    def move(obj, pos=(0, 0), time=0):
        time = float(time) / 1000
        distance = speed * time
        dx = round(distance * angle_cos)
        dy = round(distance * angle_sin)
        x, y = pos
        return x + dx, y - dy

    return move


def aimed(self, heroine, speed=100):
    angle = math.atan((self.pos[0] - heroine.pos[0]) / (self.pos[1] - heroine.pos[1]))
    return linear(angle=angle, speed=speed)


def quadratic():
    pass


def spiral():
    pass


def square_root():
    pass