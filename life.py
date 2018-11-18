from pico2d import *
import turtle as t

class LIFE:
    bar = None
    life = None
    def __init__(self):
        self.x = 540
        self.y = 470
        self.image_x = 0
        self.timer = 0
        if LIFE.bar == None:
            LIFE.bar = load_image('resource/UI/life bar2.png')
        if LIFE.life == None:
            LIFE.life = load_image('resource/UI/life.png')
        pass

    def update(self):
        self.timer += 1
        if self.timer > 20:
            self.image_x += 1
            self.timer = 0
        pass

    def draw(self):
        self.bar.clip_draw(0, 0, 803 - self.image_x, 90, self.x - int(self.image_x / 2), self.y, 750 - self.image_x, 65)
        self.life.clip_draw(0, 0, 88, 101, 160, 470 + 10, 50, 55)

        pass
