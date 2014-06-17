from enemy import *


def dummy_enemy(pos):
    # attacking = ('after', 10, 'attack every', 200, 'with', 'RedPellet', 'linear', {'angle': 100, 'speed': 200})
    # attacking = ('at', (10, 20, 30,), 'with', 'RedPellet', 'linear', {'angle': 100, 'speed': 200})
    return Enemy, {'pos': pos}

# TODO - create a fixed list of enemy spawn points?
# TODO - 'top', 'left' and 'right' - constants for one of coordinates

steps = [
    [(3000, dummy_enemy((x, 100))) for x in range(100, 700, 100)],
    [(6000, dummy_enemy((x, 200))) for x in range(100, 700, 100)],
    [(9000, dummy_enemy((x, 300))) for x in range(100, 700, 100)],
]

# Flatten lists of lists
# Help: http://rhodesmill.org/brandon/2009/nested-comprehensions/
scenario = [action for step in steps for action in step]
