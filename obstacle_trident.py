from pico2d import *
import obstacle
import game_framework
import cookie_brave as brave
import scene_main

TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8


class Trident(obstacle.Obstacle):
    image = None

    def __init__(self, row, col):
        if Trident.image == None:
            Trident.image = load_image('resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_1.png')

        self.frame = 0
        self.time = 0
        self.speed = 200
        self.x = ((106 * 12) * col + 106 * row - brave.Brave().x + 118)
        self.y = 500 / 2 - 110
        self.type = 6
        pass

    def update(self):
        if scene_main.cookie.die_animation:
            self.speed = 0
        self.x -= self.speed * game_framework.frame_time
        if brave.Brave().x + 300 < self.x:
            self.frame = 0
        elif brave.Brave().x + 300 > self.x:
            self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4

        if self.frame >= 3:
            self.frame = 3
        pass

    def draw(self):
        if self.x < 1100:
            Trident.image.clip_draw(int(self.frame) * 100, 0, 100, 140, self.x, self.y)
            draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - 34, self.y - 70, self.x, self.y + 20