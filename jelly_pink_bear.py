from pico2d import *
import game_framework
import jelly


class PinkBear(jelly.Jelly):
    image = None
    def initialize(self):
        if PinkBear.image == None:
            PinkBear.image = load_image('resource/Cookie Skill Effects and Jellies/jelly/simple bear.png')
        self.image_x = 1
        pass

    def draw(self):
        if self.x < 1000.0:
            self.image.clip_draw(self.image_x * 60, self.image_y, 60, 60, self.x, self.y, 32, 32)
            draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - 15, self.y - 14, self.x + 15, self.y + 14
        pass