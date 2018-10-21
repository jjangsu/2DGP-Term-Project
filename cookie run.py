import game_framework
import pico2d

import scene_main


pico2d.open_canvas(1000, 500)
game_framework.run(scene_main)
pico2d.close_canvas()