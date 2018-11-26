from pico2d import *
import game_framework
import jelly


TIME_PER_ACTION = 0.4
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 6


class SilverCoin(jelly.Jelly):
    image = None

    def initialize(self):
        if SilverCoin.image == None:
            SilverCoin.image = load_image('resource/Cookie Skill Effects and Jellies/jelly/silver coin.png')
        self.type = 3
        pass

    def update(self):
        self.x -= self.speed * game_framework.frame_time
        self.image_x = (self.image_x + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 4
        pass

    def draw(self):
        if self.x < 1000.0:
            SilverCoin.image.clip_draw(int(self.image_x) * 50, self.image_y, 50, 50, self.x, self.y, 30, 30)
            draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - 15, self.y - 14, self.x + 15, self.y + 14
        pass