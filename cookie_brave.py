import cookie
from pico2d import *


class Brave(cookie.Character):
    def newPosition(self, x, y):
        self.x = x
        self.y = y
        self.standard_time = 3.5
        self.image = load_image('resource/character/Brave Cookie.png')
        self.crash_x1 = 0
        self.crash_x2 = 40
        self.crash_y1 = 120
        self.crash_y2 = 0
        self.jump_sound = load_wav('sound/effect sound/ch01jump.wav')
        self.Double_jump_sound = load_wav('sound/effect sound/ch01jump.wav')
        self.slide_sound = load_wav('sound/effect sound/ch01slide.wav')
        pass

    def get_bb(self):
        return self.x + self.crash_x1, self.y - self.crash_y1, self.x + self.crash_x2, self.y + self.crash_y2
