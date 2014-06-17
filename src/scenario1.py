import common
from enemy import *


def dummy_enemy(pos):
    # TODO - attack params
    # attacking = ('after', 10, 'attack every', 200, 'with', 'RedPellet', 'linear', {'angle': 100, 'speed': 200})
    # attacking = ('at', (10, 20, 30,), 'with', 'RedPellet', 'linear', {'angle': 100, 'speed': 200})
    # TODO - no lambdas
    # TODO - return type-params tuple
    return lambda: Raven(pos)

# TODO - convert lambdas to param lists
# TODO - create enemies inside game loop
# TODO - create a fixed list of enemy spawn points?
# TODO - 'top', 'left' and 'right' - constants for one of coordinates
# TODO - list comprehensions instead of maps
# [(3000, dummy_enemy((x, 'top'))) for x in range(100, 700, 100)]

steps = [
    map(lambda x: (3000, dummy_enemy((x, 100))), range(100, 700, 100)),
    map(lambda x: (6000, dummy_enemy((x, 200))), range(100, 700, 100)),
    map(lambda x: (9000, dummy_enemy((x, 300))), range(100, 700, 100)),
]

# Flatten lists of lists
# Help: http://rhodesmill.org/brandon/2009/nested-comprehensions/
scenario = [action for step in steps for action in step]
