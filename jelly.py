import game_framework
import scene_main
import cookie_brave


class Jelly:
    def __init__(self, row, col):
        self.x = cookie_brave.Brave().x + 600 + col * 30
        self.y = 110 + row * 25
        self.speed = 200
        self.image_x = 0
        self.image_y = 0

        self.type = 0
        pass


    def update(self):
        self.x -= self.speed * game_framework.frame_time
        if scene_main.cookie.die_animation:
            self.speed = 0
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
        return True
        pass

