from pico2d import *
import game_framework
import game_world
import character_brave


class Pin_bean:
    image = None
    t = 0
    def __init__(self, row, col):
        if Pin_bean.image == None:
            Pin_bean.image = load_image('resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_jp1B.png')
        Pin_bean.t += 1
        self.x = ((106 * 12) * col + 106 * row - character_brave.Brave().x + 118) # 106 * ( 12 * col + row) # 93
        self.y = 70 + 45 # 115
        self.speed = 200
        self.row = row
        self.col = col
        pass

    def update(self):
        # print(str(self.col) + ' ' + str(self.row))
        self.x -= self.speed * game_framework.frame_time
        if self.x < -110:
            game_world.remove_object(self)
        pass

    def draw(self):
        if self.x < 1100:
            self.image.clip_draw(0, 0, 68, 99, self.x, self.y)
            draw_rectangle(*self.get_bb())
        pass

    def get_bb(self):
        return self.x - 34, self.y - 47, self.x + 34, self.y + 47
