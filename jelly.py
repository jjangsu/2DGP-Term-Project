import game_framework
import obstacle
import cookie_brave
import game_world

i = 0


class Jelly:
    def __init__(self, row, col):
        self.x = cookie_brave.Brave().x + 600 + col * 30
        self.y = 110 + row * 25
        #print(row)
        #print(self.y)
        self.speed = 200
        # self.image = (route)
        self.image_x = 0
        self.image_y = 0
        pass

    def newPosition(self, obs):
        global p1_x, p1_y, p2_x, p2_y, p3_x, p3_y, t, i

        if obs.type == 1 or obs.type == 6:
            p1_x, p1_y = obs.x - 50, 95
            p2_x, p2_y = obs.x - 10, obs.y + 80
            p3_x, p3_y = obs.x + 110, 95

            t = i / 100.0
            self.y = (2 * t ** 2 - 3 * t + 1) * p1_y + (-4 * t ** 2 + 4 * t) * p2_y + (2 * t ** 2 - t) * p3_y
            i += 20
            if i > 100:
                i = 0


        elif obs.type == 2:
            # self.y = 270
            p1_x, p1_y = obs.x - 40, 95
            p2_x, p2_y = obs.x, obs.y + 120
            p3_x, p3_y = obs.x + 120, 95
            t = i / 100.0
            self.y = (2 * t ** 2 - 3 * t + 1) * p1_y + (-4 * t ** 2 + 4 * t) * p2_y + (2 * t ** 2 - t) * p3_y
            i += 18
            if i > 100:
                i = 0
            pass


        elif obs.type == 3 :
            self.y = 95


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

