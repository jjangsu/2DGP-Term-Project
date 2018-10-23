from pico2d import *

class Bright:
    image = None
    def __init__(self):
        self.x = 200
        self.y = 70 + 115
        self.frame = 0
        self.image_y = 4
        if Bright.image == None:
            Bright.image = load_image('resource/Bright Cookie.png')
        self.time = 0
        pass

    def newPosition(self, x, y):
        self.x = x
        self.y = y
        pass

    def update(self):
        self.time += 1
        if self.time > 2:
            self.frame = (self.frame + 1) % 4
            self.time = 0
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 236, self.image_y * 236, 236, 236, self.x, self.y)
        pass