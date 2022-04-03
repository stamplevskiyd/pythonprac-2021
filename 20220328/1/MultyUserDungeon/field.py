"""Base configuration for multi-user dungeon."""


class Cell:
    """One cell on the map."""

    def __init__(self, X, Y, monster_n, monster_h):
        """Create cell with given coords and monster."""
        self.x = X
        self.y = Y
        self.monster_name = monster_n
        self.health = monster_h


field_width = 10
field_height = 10
prompt = '> '
