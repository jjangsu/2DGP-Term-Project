from pico2d import *

class FPS:
    def __init__(self):
        self.lastTime = get_time()
        self.elapsed = 1
        self.lag = 0.0
        self.MS_PER_UPDATE = 8
        pass

    def update(self):
        self.current = get_time()
        self.elapsed = self.current - self.lastTime
        self.lastTime = self.current
        pass
