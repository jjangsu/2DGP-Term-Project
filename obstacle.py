import cookie_brave
import game_world
import game_framework
from pico2d import *

class Obstacle:
    def __init__(self, row, col):
        self.x = ((106 * 12) * col + 106 * row - cookie_brave.Brave().x + 118)
        self.y = 70
        self.speed = 200
        self.image = None

        self.frame = 0
        self.time = 0

        self.timer = 0
        self.type = 0

    def update(self):
        # global obstacle_type
        self.x -= self.speed * game_framework.frame_time
        # print(self.x)
        # if self.x < - 100:
        #     game_world.remove_object(self)

