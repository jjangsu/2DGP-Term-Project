import game_framework
import obstacle
import cookie_brave
import game_world

i = 0

class Jelly:
    angle = 20
    pi = 3.14

    def __init__(self, row, col):
        self.x = cookie_brave.Brave().x + 600 + col * 15
        self.y = 160 + row * 20
        self.speed = 200
        # self.image = None
        self.image_x = 0
        self.image_y = 0
        pass

    def newPosition(self, obs):
         # radian = Jelly.angle / 180 * Jelly.pi
        # # .y = 1 / ()          # 200 * math.sin(radian)
        # print(Jelly.angle)
        # print(self.y)
        # Jelly.angle += 10
        # # print(Jelly.angle)
        # if Jelly.angle > 180:
        #     Jelly.angle = 0
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

