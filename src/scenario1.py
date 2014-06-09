import common
from enemy import *


def dummy_enemy(pos):
    return lambda: Enemy(pos)


scenario = map(lambda x: (3000, dummy_enemy((x, 100))), range(100, 600, 100)) + \
           map(lambda x: (6000, dummy_enemy((x, 200))), range(100, 600, 100)) + \
           map(lambda x: (9000, dummy_enemy((x, 300))), range(100, 600, 100))
