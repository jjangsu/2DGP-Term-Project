from pico2d import *
import random
import os

import game_framework

name = "background_state"
background = None

class Background:
    def __init__(self):
        self.image = load_image('resource/background.png')
        self.image2 = load_image('resource/background1.png')
        self.path = load_image('resource/Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_tb1.png')
        pass

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 1000, 500, 500, 250)
        self.image2.clip_draw(0, 0, 1000, 100, 500, 50)
        for n in range(10):
            self.path.clip_draw(0, 0, 124, 120, 124 * n, 10)
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

