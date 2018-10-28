from pico2d import *
import fps

class Path:
    path = None
    def __init__(self, i):
        if Path.path == None:
            self.path = load_image('resource/Episode 1 - Escape from the Oven/1. The Witch Oven/epN01_tm01_tb1.png')
        self.path_x = i * 124
        pass

    def update(self):
        self.path_x -= 1.0 * fps.FPS().elapsed
        if self.path_x < -62:
            self.path_x = 124*10-62
        pass

    def draw(self):
        self.path.clip_draw(0, 0, 124, 120, self.path_x, 10)
        pass
