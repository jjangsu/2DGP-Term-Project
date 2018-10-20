from pico2d import *

class Fork_sky:
    image = None
    def __init__(self, row, col):
        if Fork_sky.image == None:
            self.image = load_image('resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_sdA.png')
            self.x = (106 * 9) * col + 106 * row
            self.y = 500 - 120
        pass

    def update(self):
        self.x -= 1.0
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 86, 482, self.x, self.y)
        pass