import imp
import random
import constants
from game.casting.actor import Actor
from game.shared.point import Point
from game.casting.player2 import Player2


class Bullet(Actor):
    """
    A tasty item that snakes like to eat.
    
    The responsibility of Food is to select a random position and points that it's worth.

    Attributes:
        _points (int): The number of points the food is worth.
    """
    def __init__(self):
        "Constructs a new Food."
        super().__init__()
        self.set_text('B')
        self.set_color(constants.WHITE)
        self.start()
        self._shot_fired = False
    def start(self):
        player = Player2()
        head = player.get_head()
        position = head.get_position()
        # x = int(constants.MAX_X / 2)
        # y = int(constants.MAX_Y - 15)
        # position = Point(x,y)
        self.set_position(position)
    
    def shoot(self, velocity):
        self.set_velocity(velocity)
    
    def get_shot_fired(self):
        return self._shot_fired
    def set_shot_fired(self, fired):
        self._shot_fired = fired
