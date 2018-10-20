from pico2d import *
import random
import os
import path

import game_framework

name = "background_state"
background = None

class Background:
    def __init__(self):
        self.background = load_image('resource/background.png')
        self.background2 = load_image('resource/background.png')
        self.fire = load_image('resource/background1.png')
        self.fire2 = load_image('resource/background1.png')
        self.backGround_x = 500
        self.backGround_x2 = 1500
        self.fire_x = 500
        self.fire_x2 = 1500

        # self.path[]
        pass

    def update(self):
        self.backGround_x -= 0.3
        self.backGround_x2 -= 0.3
        if (self.backGround_x < -500):
            self.backGround_x = 1500
        if self.backGround_x2 < -500:
            self.backGround_x2 = 1500

        self.fire_x -= 0.5
        self.fire_x2 -= 0.5
        if(self.fire_x < -500):
            self.fire_x = 1500
        if (self.fire_x2 < -500):
            self.fire_x2 = 1500


        pass

    def draw(self):
        self.background.clip_draw(0, 0, 1000, 500, self.backGround_x, 250)
        self.background.clip_draw(0, 0, 1000, 500, self.backGround_x2, 250)
        self.fire.clip_draw(0, 0, 1000, 100, self.fire_x, 50)
        self.fire2.clip_draw(0, 0, 1000, 100, self.fire_x2, 50)

        pass




def enter():
    global background, paths
    background = Background()
    paths = [path.Path(n) for n in range(10)]
    pass


def exit():
    global background, paths
    del (background)
    del (paths)
    pass


def update():
    global background, paths
    background.update()
    for path in paths:
        path.update()
    pass


def draw():
    global background, paths
    clear_canvas()
    background.draw()
    for path in paths:
        path.draw()
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




