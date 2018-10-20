import pin_bean_obstacle
import fork_sausage_obstacle

class Obstacle:
    def __init__(self, obstacle_type, row, col):
        if obstacle_type == 1:
            self.type = pin_bean_obstacle.Pin_bean(row, col)
        elif obstacle_type == 2:
            self.type = fork_sausage_obstacle.Fork_sausage(row, col)

    def update(self):
        self.type.update()
        pass

    def draw(self):
        self.type.draw()
        pass


