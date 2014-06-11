class Position(object):
    """Sprite position reusable property

       https://docs.python.org/2/howto/descriptor.html
    """

    def __init__(self, initial_value=(0, 0), callback=None):
        self.value = initial_value
        self.callback = callback

    def __get__(self, instance, instance_type=None):
        return instance.rect.center

    def __set__(self, instance, new_pos):
        instance.rect.center = new_pos
        if self.callback:
            getattr(instance, self.callback)()




