from pico2d import *
import game_framework
import game_world
import character_brave

class Fork_sausage:
    image = None
    def __init__(self, row, col):
        if Fork_sausage.image == None:
            Fork_sausage.image = load_image('resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_jp2B.png')
        self.x = ((106 * 12) * col + 106 * row - character_brave.Brave().x + 118) # 106 * ( 12 * col + row)
        self.y = 70 + 92
        self.speed = 200
        pass

    def update(self):
        self.x -=  self.speed * game_framework.frame_time
        if self.x < -100:
            game_world.remove_object(self)
        pass

    def draw(self):
        if self.x < 1100:
            self.image.clip_draw(0, 0, 106, 193, self.x, self.y)
        pass