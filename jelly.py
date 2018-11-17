import game_framework
from pico2d import *


class Jelly:
    def __init__(self, row, col):
        self.x = 850 + col * 5
        self.y = 95 + row * 20
        self.speed = 200
        # self.image = None
        self.image_x = 0
        self.image_y = 0
        pass

    def update(self):
        self.x -= self.speed * game_framework.frame_time
        pass

    def collide_obstacle(self):
        pass

