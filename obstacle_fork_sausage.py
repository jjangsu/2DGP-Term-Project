from pico2d import *
import obstacle
import cookie_brave


class Fork_sausage(obstacle.Obstacle):
    image = None

    def __init__(self, row, col):
        # if Fork_sausage.image == None:
        Fork_sausage.image = load_image('resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_jp2B.png')
        self.y = 70 + 92
        self.x = ((106 * 12) * col + 106 * row - cookie_brave.Brave().x + 118)
        self.speed = 200
        self.type = 2
        pass

    def draw(self):
        if self.x < 1100:
            Fork_sausage.image.clip_draw(0, 0, 106, 193, self.x, self.y)
            draw_rectangle(*self.get_bb())
        if self.x < - 100:
            del (self)
        pass

    def get_bb(self):
        return self.x - 40, self.y - 90, self.x, self.y + 60
        pass
