from pico2d import *
import obstacle
import cookie_brave
import scene_main


class Pin_bean(obstacle.Obstacle):
    image = None

    def __init__(self, row, col):
        if Pin_bean.image == None:
            Pin_bean.image = load_image('resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_jp1B.png')
        self.y = 70 + 45 # 115
        self.x = ((106 * 12) * col + 106 * row - cookie_brave.Brave().x + 118)
        self.speed = 200
        self.type = 1
        pass

    def draw(self):
        if scene_main.cookie.die_animation:
            self.speed = 0
        if self.x < 1100 :
            Pin_bean.image.clip_draw(0, 0, 68, 99, self.x, self.y)
            draw_rectangle(*self.get_bb())
        if self.x < - 100:
            del (self)
        pass

    def get_bb(self):
        return self.x - 34, self.y - 47, self.x, self.y + 47
