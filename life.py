from pico2d import *

class LIFE:
    image = None
    def __init__(self):
        self.x = 500
        self.y = 470
        if LIFE.image == None:
            LIFE.image = load_image('resource/life bar.png')
        pass

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 865, 90, self.x, self.y, 750, 65)
        pass
