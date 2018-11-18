import game_framework
from pico2d import *
import cookie_brave


class Jelly:
    def __init__(self, row, col):
        self.x = cookie_brave.Brave().x + 600 + col * 30
        self.y = 110 + row * 25
        self.speed = 200
        # self.image = load_image('resource/Cookie Skill Effects and Jellies/jelly/General Jellies.png')
        self.image_x = 0
        self.image_y = 0
        pass


    def update(self):
        self.x -= self.speed * game_framework.frame_time
        # if self.x < -10:
        #     game_world.remove_object(self)
        pass

    def get_bb(self):
        return self.x - 10, self.y - 14, self.x + 10, self.y + 14
        pass

    def collide_obstacle(self, b):
        left_a, bottom_a, right_a, top_a = self.get_bb()
        left_b, bottom_b, right_b, top_b = b.get_bb()
        if left_a > right_b + 50:
            return False
        if right_a < left_b - 30:
            return False
        # if top_a < bottom_b:
        #     return False
        # if bottom_a > top_b:
        #     return False

        return True
        pass

