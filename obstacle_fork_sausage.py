from pico2d import *

class Fork_sausage:
    image = None
    def __init__(self, row, col):
        if Fork_sausage.image == None:
            Fork_sausage.image = load_image('resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_jp2B.png')
        self.x = (105 * 12) * col + 105 * row
        self.y = 70 + 92
        pass

    def update(self):
        self.x -= 2.0
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 106, 193, self.x, self.y)
        pass