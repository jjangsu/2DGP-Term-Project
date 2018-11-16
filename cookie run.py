import game_framework
import pico2d

import scene_start


pico2d.open_canvas(1000, 500)
game_framework.run(scene_start)
pico2d.close_canvas(sync = True)