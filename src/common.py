from pygame.sprite import Group, LayeredDirty, OrderedUpdates

# Groups
heroine_shots_group = Group()
enemy_shots_group = Group()
all_shots_group = Group()
enemies_group = Group()
explosions_group = Group()
bonuses_group = Group()
indicators_group = Group()
everything_group = OrderedUpdates()

# Heroine reference
heroine = None

# Layer order constants
LAYERS = {}

# Playfield reference
playfield_boundary = None