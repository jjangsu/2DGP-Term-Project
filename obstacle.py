import random

import obstacle_pin_bean
import obstacle_fork_sausage
import obstacle_fork_sky
import obstacle_fly_stone

class Obstacle:
    def __init__(self, obstacle_type, row, col):
        if obstacle_type == 1:
            self.type = obstacle_pin_bean.Pin_bean(row, col)
        elif obstacle_type == 2:
            self.type = obstacle_fork_sausage.Fork_sausage(row, col)
        elif obstacle_type == 3:
            self.type = obstacle_fork_sky.Fork_sky(row, col)
        elif obstacle_type == 4:
            self.type = random.randint(0, 1)
            self.type = obstacle_fly_stone.Fly_stone(row, col, self.type)

    def update(self):
        self.type.update()
        pass

    def draw(self):
        self.type.draw()
        pass


