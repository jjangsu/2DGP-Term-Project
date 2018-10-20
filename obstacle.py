from pico2d import *

class Obstacle:
    pin_bean = None
    def __init__(self):
        if Obstacle.pin_bean == None:
            self.pin_bean = load_image('resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_jp1B.png')
        self.pin_bean_x = 124 * 9
        self.pin_bean_y = 115
        pass

    def update(self):
        self.pin_bean_x -= 1.0
        pass

    def draw(self):
        self.pin_bean.clip_draw(0, 0, 68, 99, self.pin_bean_x, self.pin_bean_y)
        pass