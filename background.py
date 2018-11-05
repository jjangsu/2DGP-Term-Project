from pico2d import *
import game_framework
import random
import os

name = "background_state"

class Background:
    background = None
    background2 = None
    fire = None
    fire2 = None

    def __init__(self):
        if Background.background == None:
            Background.background = load_image('resource/background.png')
        if Background.background2 == None:
            Background.background2 = load_image('resource/background.png')
        if Background.fire == None:
            Background.fire = load_image('resource/background1.png')
        if Background.fire2 == None:
            Background.fire2 = load_image('resource/background1.png')
        self.backGround_x = 500
        self.backGround_x2 = 1500
        self.fire_x = 500
        self.fire_x2 = 1500
        self.speed_1 = 80.0
        self.speed_2 = 100.0

        # self.path[]
        pass

    def update(self):
        self.backGround_x -= self.speed_1 * game_framework.frame_time
        self.backGround_x2 -= self.speed_1 * game_framework.frame_time
        if (self.backGround_x < -500):
            self.backGround_x = 1500
        if self.backGround_x2 < -500:
            self.backGround_x2 = 1500

        self.fire_x -= self.speed_2 * game_framework.frame_time
        self.fire_x2 -= self.speed_2 * game_framework.frame_time
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







