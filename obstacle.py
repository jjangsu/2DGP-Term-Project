import pin_bean_obstacle
import fork_sausage_obstacle

class Obstacle:
    def __init__(self, obstacle_type, row, col):
        if obstacle_type == 1:
            self.type_1 = pin_bean_obstacle.Pin_bean(row, col)

    def update(self):
        self.type_1.update()
        pass

    def draw(self):
        self.type_1.draw()
        pass


