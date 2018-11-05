from pico2d import *
import obstacle
import character_brave


class Fork_sausage(obstacle.Obstacle):
    image = None

    def __init__(self, row, col):
        # if Fork_sausage.image == None:
        Fork_sausage.image = load_image('resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_jp2B.png')
        self.y = 70 + 92
        self.x = ((106 * 12) * col + 106 * row - character_brave.Brave().x + 118)
        self.speed = 200
        pass

    def draw(self):
        if self.x < 1100:
            Fork_sausage.image.clip_draw(0, 0, 106, 193, self.x, self.y)
            draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - 50, self.y - 100, self.x + 50, self.y + 100
        pass
