import time

class FPS:
    def __init__(self):
        self.lastTime = time.time()
        self.elapsed = 0
        self.lag = 0.0
        self.MS_PER_UPDATE = 8
        pass

    def update(self):
        self.current = time.time()
        self.elapsed = self.current - self.lastTime
        self.lastTime = self.current
        self.lag += self.elapsed
        pass
