import character
from pico2d import *


class Bright(character.Character):
    def newPosition(self, x, y):
        self.x = x
        self.y = y
        self.standard_time = 3.5
        self.image = load_image('resource/Bright Cookie.png')
        pass

    def get_bb(self):
        return self.x - 10, self.y - 120, self.x + 40, self.y + 0