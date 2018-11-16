import cookie
from pico2d import *


class Bright(cookie.Character):
    def newPosition(self, x, y):
        self.x = x
        self.y = y
        self.standard_time = 3.5
        self.image = load_image('resource/character/Bright Cookie.png')
        self.crash_x1 = 0
        self.crash_x2 = 40
        self.crash_y1 = 120
        self.crash_y2 = 0
        pass

    def get_bb(self):
        return self.x + self.crash_x1, self.y - self.crash_y1, self.x + self.crash_x2, self.y + self.crash_y2
