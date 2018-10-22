from pico2d import *

class Brave():
    def __init__(self):
        self.x = 200
        self.y = 70 + 115
        self.image_y = 4
        self.frame = 0
        self.image = load_image('resource/Brave Cookie.png')
        self.time = 0
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