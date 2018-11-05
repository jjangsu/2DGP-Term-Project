import random
import obstacle
import game_framework
import game_world
from pico2d import *


TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Fly_stone(obstacle.Obstacle):
    def enter(self):
        self.frame = 0
        self.time = 0
        self.speed = 400
        self.image = load_image(
            'resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_bl1_ing_sprite.png')
        # self.stone_type = random.randint(0, 1)
        # if self.stone_type == 0:
        #     self.fly_stone = obstacle_fly_stone_1.Stone_1(row, col)#
        # elif self.stone_type == 1:
        #     self.fly_stone = obstacle_fly_stone_4.Stone_4(row, col)
        pass

    def update(self):
        self.x -= self.speed * game_framework.frame_time
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
        # self.fly_stone.update()
        pass

    # def draw(self):
    #     if self.x < 1100:
    #         self.image.clip_draw(int(self.frame) * 200, 0, 202, 117, self.x, self.y)
    #         draw_rectangle(*self.get_bb())
    #     # self.fly_stone.draw()
    #     pass
    #