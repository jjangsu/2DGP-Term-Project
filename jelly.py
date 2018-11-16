import game_framework


class Jelly:
    def __init__(self):
        self.x = 850
        self.y = 85
        self.speed = 200
        self.image = None
        self.image_x = 0
        self.image_y = 0
        pass

    def update(self):
        self.x -= self.speed * game_framework.frame_time
        pass

