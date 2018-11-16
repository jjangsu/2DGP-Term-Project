from pico2d import *
import obstacle
import cookie_brave

class Fork_sky(obstacle.Obstacle):
    image = None

    def __init__(self, row, col):
        # if Fork_sky.image == None:
        Fork_sky.image = load_image('resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_sdA.png')
        self.y = 500 - 120
        self.x = ((106 * 12) * col + 106 * row - cookie_brave.Brave().x + 118)
        self.speed = 200
        pass


    def draw(self):#
        if self.x < 1100:
            Fork_sky.image.clip_draw(0, 0, 86, 482, self.x, self.y)
            draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - 40, self.y - 240, self.x + 20, self.y + 200
        pass