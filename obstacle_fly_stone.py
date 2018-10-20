import random
import obstacle_fly_stone_1
import obstacle_fly_stone_4

class Fly_stone:
    def __init__(self, row, col):
        self.stone_type = random.randint(0, 1)
        if self.stone_type == 0:
            self.fly_stone = obstacle_fly_stone_1.Stone_1(row, col)
        elif self.stone_type == 1:
            self.fly_stone = obstacle_fly_stone_4.Stone_4(row, col)
        pass

    def update(self):
        self.fly_stone.update()
        pass

    def draw(self):
        self.fly_stone.draw()
        pass
