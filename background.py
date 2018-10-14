from pico2d import *
import random
import os

import game_framework

name = "background_state"
background = None

class Background:
    def __init__(self):
        self.image = load_image('resource/background.png')
        pass

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw(0, 0, 900, 500, 450, 250)
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

