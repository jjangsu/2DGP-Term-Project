from pico2d import *
import random
import os

import game_framework

name = "background_state"
background = None

class Background:
    def __init__(self):
        self.background = load_image('resource/background.png')
        self.background2 = load_image('resource/background.png')
        self.fire = load_image('resource/background1.png')
        self.fire2 = load_image('resource/background1.png')
        self.path = load_image('resource/Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_tb1.png')
        self.backGround_x = 500
        self.backGround_x2 = 1500
        self.fire_x = 500
        self.fire_x2 = 1500
        self.path_x = 124

        # self.path[]
        pass

    def update(self):
        self.backGround_x -= 0.1
        self.backGround_x2 -= 0.1
        if (self.backGround_x < -500):
            self.backGround_x = 1500
        if self.backGround_x2 < -500:
            self.backGround_x2 = 1500

        self.fire_x -= 0.3
        self.fire_x2 -= 0.3
        if(self.fire_x < -500):
            self.fire_x = 1500
        if (self.fire_x2 < -500):
            self.fire_x2 = 1500

        self.path_x -= 0.5
        if self.path_x < -124:
            self.path_x = 1240
        pass

    def draw(self):
        self.background.clip_draw(0, 0, 1000, 500, self.backGround_x, 250)
        self.background.clip_draw(0, 0, 1000, 500, self.backGround_x2, 250)
        self.fire.clip_draw(0, 0, 1000, 100, self.fire_x, 50)
        self.fire2.clip_draw(0, 0, 1000, 100, self.fire_x2, 50)
        for n in range(10):
            self.path.clip_draw(0, 0, 124, 120, self.path_x * n, 10)
        pass

class Path:
    def __init__(self):
        pass

    def update(self):
        pass

    def draw(self):
        pass


def enter():
    global background
    background = Background()
    pass


def exit():
    global background
    del (background)
    pass


def update():
    global background
    background.update()
    pass


def draw():
    global background
    clear_canvas()
    background.draw()
    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
    pass


def pause():
    pass


def resume():
    pass

