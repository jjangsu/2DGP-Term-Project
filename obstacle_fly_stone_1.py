from pico2d import *
import obstacle
import game_framework
import cookie_brave

TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Stone_1(obstacle.Obstacle):
    image = None

    def __init__(self, row, col):
        # if Stone_1.image == None:
        self.frame = 0
        self.time = 0
        self.speed = 400
        Stone_1.image = load_image('resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_bl1_ing_sprite.png')
        self.x = ((106 * 12) * col + 106 * row - cookie_brave.Brave().x + 118) * 2
        self.y = 500 / 2 - 140
        self.type = 4
        pass

    def update(self):
        self.x -= self.speed * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        # self.fly_stone.update()
        pass

    def draw(self):
        if self.x < 1100:
            Stone_1.image.clip_draw(int(self.frame) * 200, 0, 202, 117, self.x, self.y)
            draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - 50, self.y - 38, self.x + 34, self.y + 35
        pass
