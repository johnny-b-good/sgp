import common
from enemy import *


def dummy_enemy(pos):
    return lambda: Raven(pos)


scenario = map(lambda x: (3000, dummy_enemy((x, 100))), range(100, 700, 100)) + \
           map(lambda x: (6000, dummy_enemy((x, 200))), range(100, 700, 100)) + \
           map(lambda x: (9000, dummy_enemy((x, 300))), range(100, 700, 100))
