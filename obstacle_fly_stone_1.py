from pico2d import *
import character
import fps

class Stone_1:
    image = None

    def __init__(self, row, col):
        if Stone_1.image == None:
            Stone_1.image = load_image(
                'resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_bl1_ing_sprite.png')
        self.x = ((106 * 12) * col + 106 * row - character.Character(1).x + 118) * 2
        self.y = 500 / 2 - 140
        self.frame = 0
        self.time = 0
        pass

    def update(self):
        self.x -= 4.0 * fps.FPS().elapsed
        self.time += 1
        if self.time > 20:
            self.frame = (self.frame + 1) % 3
            self.time = 0
        pass

    def draw(self):
        if self.x < 1100 and self.x > -100:
            self.image.clip_draw(self.frame * 200, 0, 202, 117, self.x, self.y)
        pass