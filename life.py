from pico2d import *

class LIFE:
    image = None
    def __init__(self):
        self.x = 200
        self.y = 400
        if LIFE.image == None:
            LIFE.image = load_image('resource/life.png')
        pass

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 88, 101, self.x, self.y)
        pass
