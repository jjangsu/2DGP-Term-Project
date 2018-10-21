from pico2d import *

class Character:
    def __init__(self, type):
        self.x = 200
        self.y = 70 + 115
        self.frame = 1
        self.image_y = 4
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