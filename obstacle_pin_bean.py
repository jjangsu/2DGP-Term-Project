from pico2d import *
import fps

class Pin_bean:
    image = None
    def __init__(self, row, col):
        if Pin_bean.image == None:
            Pin_bean.image = load_image('resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_jp1B.png')
        self.x = (106 * 12) * col + 106 * row
        self.y = 70 + 45 # 115
        pass

    def update(self):
        self.x -= 2.0 * fps.FPS().elapsed
        pass

    def draw(self):
        if self.x < 1100 and self.x > -100:
            self.image.clip_draw(0, 0, 68, 99, self.x, self.y)
        pass