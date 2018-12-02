from pico2d import *
import game_framework
import scene_main

class Path:
    path = None
    def __init__(self, i):
        if Path.path == None:
            self.path = load_image('resource/Episode 1 - Escape from the Oven/1. The Witch Oven/path ground.png')
        self.path_x = i * 1240 + 500
        self.speed = 200
        pass

    def update(self):
        self.path_x -= self.speed * game_framework.frame_time

        if self.path_x < -620:
            self.path_x = 1000 + 1240 // 2

        if scene_main.cookie.die_animation:
            self.speed = 0
        pass

    def draw(self):
        self.path.clip_draw(0, 0, 1240, 120, self.path_x, 10)
        pass

