from pico2d import *
import random

class Fly_stone:
    image = None
    def __init__(self, row, col, type):
        if Fly_stone.image == None:
            self.image = load_image(
                'resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_bl1_ing_sprite.png')
            self.x = (106 * 9) * col + 106 * row
            self.y = 500 / 2 - 140
            self.frame = 0
            self.time = 0
        pass

    def update(self):
        self.x -= 1.0
        self.time += 1
        if self.time > 20:
            self.frame = (self.frame + 1) % 3
            self.time = 0
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 200, 0, 202, 117, self.x, self.y)
        pass
