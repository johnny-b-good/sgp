from enemy import *
import projectile as p
import attack as a
import movement as m


def dummy_enemy(pos):
    attack_params = {'projectile_type': p.RedPellet, 'movement_type': m.linear, 'movement_params': {'speed': 200, 'angle': 270}}
    attack = {'from': 1000, 'times': 9000, 'every': 1000, 'attack_type': a.single, 'attack_params': attack_params}
    return Enemy, {'pos': pos, 'attack': attack}

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
