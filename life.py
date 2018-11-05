from pico2d import *
import turtle as t

class LIFE:
    bar = None
    life = None
    def __init__(self):
        self.x = 500
        self.y = 470
        self.image_x = 0
        if LIFE.bar == None:
            LIFE.bar = load_image('resource/life bar.png')
        if LIFE.life == None:
            LIFE.life = load_image('resource/life.png')
        pass

    def update(self):
        pass

    def draw(self):
        self.bar.clip_draw(0, 0, 865 - self.image_x, 90, self.x - int(self.image_x / 2) + 1, self.y, 750 - self.image_x, 65)
        # self.life.clip_draw(0, 0, 88, 101, 160, 470 + 10, 50, 55)

        pass
