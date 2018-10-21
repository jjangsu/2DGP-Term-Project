from pico2d import *
import game_framework
import fps

top_image = None
top_image_x = 500
top_image_x_2 = 500 + 1030
bottom_image = None
bottom_image_x = 500
bottom_image_x_2 = 500 + 1314

def enter():
    global top_image, bottom_image, top_image_2
    if top_image == None:
        top_image = load_image('resource/robby_top1.png')

    if bottom_image == None:
        bottom_image = load_image('resource/robby_bottom.png')
    pass

def exit():
    global top_image, bottom_image
    del (top_image)
    del (bottom_image)
    pass


def update():
    global top_image_x, top_image_x_2, bottom_image_x, bottom_image_x_2
    top_image_x -= 0.5 * fps.FPS().elapsed
    if top_image_x <= -515:
        top_image_x = 1000 + 515
    top_image_x_2 -= 0.5 * fps.FPS().elapsed
    if top_image_x_2 <= -515:
        top_image_x_2 = 1000 + 515

    bottom_image_x -= 1.0 * fps.FPS().elapsed
    if bottom_image_x < -657:
        bottom_image_x = 1000 + 1314/2
    bottom_image_x_2 -= 1.0 * fps.FPS().elapsed
    if bottom_image_x_2 < -657:
        bottom_image_x_2 = 1000 + 1314 / 2
    pass


def draw():
    global top_image, bottom_image, top_image_2, bottom_image_x_2
    clear_canvas()
    top_image.clip_draw(0, 0, 1030, 246, top_image_x, 250 + 123)
    top_image.clip_draw(0, 0, 1030, 246, top_image_x_2, 250 + 123)
    bottom_image.clip_draw(0, 0, 1314, 394, bottom_image_x, 250 - 197)
    bottom_image.clip_draw(0, 0, 1314, 394, bottom_image_x_2, 250 - 197)
    update_canvas()
    pass


def handle_events():
    events = get_events()
    pass


def pause():
    pass


def resume():
    pass