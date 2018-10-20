import random
import obstacle_fly_stone_1

class Fly_stone:
    def __init__(self, row, col, type):
        # if Fly_stone.image == None:
        #     self.image = load_image(
        #         'resource\Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_bl1_ing_sprite.png')
        #     self.x = ((106 * 12) * col + 106 * row - 0) * 2
        #     if type == 0:
        #         self.y = 500 / 2 - 140
        #     elif type == 1:
        #         self.y = 500 / 2 - 85
        #     self.frame = 0
        #     self.time = 0
        self.stone_type = 0 #random.randint(0, 1)

        if self.stone_type == 0:
            self.fly_stone = obstacle_fly_stone_1.Stone_1(row, col)
        pass
#
    def update(self):
        self.fly_stone.update()
        pass

    def draw(self):
        self.fly_stone.draw()
        pass
