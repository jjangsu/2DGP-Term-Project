from pico2d import *
import character_brave
import game_framework
import game_world

TIME_PER_ACTION = 0.2
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

class Stone_1:
    image = None

    def __init__(self, row, col):
        if Stone_1.image == None:
            Stone_1.image = load_image(
                'resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_bl1_ing_sprite.png')
        self.x = ((106 * 12) * col + 106 * row - character_brave.Brave().x + 118) * 2
        self.y = 500 / 2 - 140
        self.frame = 0
        self.time = 0
        pass

    def update(self):
        self.x -= 40.0 * game_framework.frame_time
       #  self.time += 1
        # if self.time > 25:
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 3
            # self.time = 0

        if self.x < -100:
            game_world.remove_object(self)
        pass

    def draw(self):
        if self.x < 1100:
            self.image.clip_draw(int(self.frame) * 200, 0, 202, 117, self.x, self.y)
        pass