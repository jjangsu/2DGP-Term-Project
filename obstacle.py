from pico2d import *


class Obstacle:
    pin_bean = None
    def __init__(self, obstacle_type, row, col):
        #self.line = [[0] * 10 for i in range(2 + 1)]

        if obstacle_type == 1:
            self.pin_bean = load_image('resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_jp1B.png')
            self.pin_bean_x = (68 * 9) * col + 68 * row
            self.pin_bean_y = 115

    def update(self):
        self.pin_bean_x -= 1.0
        pass

    def draw(self):
        self.pin_bean.clip_draw(0, 0, 68, 99, self.pin_bean_x, self.pin_bean_y)
        pass


class Pin_bean:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass