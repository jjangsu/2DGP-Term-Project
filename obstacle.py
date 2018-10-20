from pico2d import *


class Obstacle:
    def __init__(self, obstacle_type, row, col):
        if obstacle_type == 1:
            self.type_1 = Pin_bean(row, col)

    def update(self):
        self.type_1.update()
        pass

    def draw(self):
        self.type_1.draw()
        pass


class Pin_bean:
    image = None
    def __init__(self, row, col):
        if Pin_bean.image == None:
            self.image = load_image('resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_jp1B.png')
        self.x = (68 * 9) * col + 68 * row
        self.y = 115
        pass

    def update(self):
        self.x -= 1.0
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 68, 99, self.x, self.y)
        pass