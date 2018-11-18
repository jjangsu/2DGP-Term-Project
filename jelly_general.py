from pico2d import *
import game_framework
import jelly
import math


TIME_PER_ACTION = 0.4
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2


class General(jelly.Jelly):
    image = None

    def initialize(self):
        if General.image == None:
            General.image = load_image('resource/Cookie Skill Effects and Jellies/jelly/simple jelly.png')
        # self.image_x = 1
        pass



    # def update(self):
    #     self.x -= self.speed * game_framework.frame_time
    #     # self.image_x = (self.image_x + FRAMES_PER_ACTION * ACTION_PER_TIME *game_framework.frame_time) % 2 + 1
    #     pass

    def draw(self):
        if self.x < 1000.0:
            General.image.clip_draw(self.image_x * 40, self.image_y, 40, 57, self.x, self.y, 20, 28.5)
            draw_rectangle(*self.get_bb())
        if self.x < -10:
            del (self)
        pass


