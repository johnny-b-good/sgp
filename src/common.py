from pygame.sprite import Group, OrderedUpdates

# Groups
everything_group = OrderedUpdates()
heroine_shots_group = Group()
enemies_group = Group()
enemy_shots_group = Group()
explosions_group = Group()
bonuses_group = Group()
indicators_group = Group()

# Heroine reference
heroine = None