from pico2d import *


class Character:
    def __init__(self):
        self.x = 200
        self.y = 70 + 115
        self.image_y = 4
        self.image_x = 0
        self.frame_num = 4
        self.frame = 0
        self.time = 0
        self.standard_time = 3.0
        self.image = None # load_image('resource/Brave Cookie.png')
        pass

    # def newPosition(self, x, y):
    #     self.x = x
    #     self.y = y
    #     pass

    def update(self):
        self.time += 1
        if self.time > self.standard_time:
            self.frame = (self.frame + 1) % self.frame_num + self.image_x
            self.time = 0
        pass

    def draw(self):
        self.image.clip_draw(self.frame * 236, self.image_y * 236, 236, 236, self.x, self.y)
        pass