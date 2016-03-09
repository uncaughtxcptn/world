from world import printer


class Player(object):
    """The  main player of the RPG world. Monsters should prepare."""
    level = 1
    life = 6

    def __init__(self, name, *args, **kwargs):
        self.name = name

    def level_up(self, inc=1):
        """Increase level by inc (default is 1). Increase life as well."""
        self.level += inc
        self.life += inc

    def display_stats(self):
        """Prints player stats (level, life, etc)"""
        stats = 'Level: {}\tLife: {}'.format(self.level, self.life)
        printer(stats)