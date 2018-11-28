from pico2d import *
import game_framework

class LIFE:
    bar = None
    life = None
    def __init__(self):
        self.x = 200
        self.y = 438
        self.image_x = 0
        self.speed = 1
        self.timer = 0
        self.speed_timer = 0
        self.speed_parameter = 0
        if LIFE.bar == None:
            LIFE.bar = load_image('resource/UI/life bar2.png')
        if LIFE.life == None:
            LIFE.life = load_image('resource/UI/life.png')
        pass

    def update(self):
        self.timer += 1
        if self.timer > 20:
            self.image_x += self.speed
            self.timer = 0
        self.speed_timer += 1
        if self.speed_timer % 1500 == 0:
            self.speed_parameter += 1.1
            self.speed = self.speed + int(self.speed_parameter + 0.5)

        pass

    def draw(self):
        self.bar.clip_draw_to_origin(0, 0, 450 - self.image_x, 90, self.x, self.y, 450 - self.image_x, 65)
        self.life.clip_draw(0, 0, 88, 101, 200, 470 + 10, 50, 55)

        pass
