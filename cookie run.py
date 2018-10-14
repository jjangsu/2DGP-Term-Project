import game_framework
import pico2d

import background


pico2d.open_canvas(900, 500)
game_framework.run(background)
pico2d.close_canvas()