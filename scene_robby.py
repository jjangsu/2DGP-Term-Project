from pico2d import *
import game_framework
import fps
import scene_main

top_image = None
top_image_x = 500
top_image_x_2 = 500 + 1030
bottom_image = None
bottom_image_x = 500
bottom_image_x_2 = 500 + 1314
mouse = None
mouse_x = 0
mouse_y = 0


def enter():
    global top_image, bottom_image, mouse
    if top_image == None:
        top_image = load_image('resource/robby_top1.png')

    if bottom_image == None:
        bottom_image = load_image('resource/robby_bottom.png')

    if mouse == None:
        hide_cursor()
        mouse = load_image('resource/mouse1.png')


    pass

def exit():
    global top_image, bottom_image, mouse
    del (top_image)
    del (bottom_image)
    del (mouse)
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
    top_image.clip_draw(0, 0, 1030, 246, top_image_x, 250 + 125)
    top_image.clip_draw(0, 0, 1030, 246, top_image_x_2, 250 + 125)
    bottom_image.clip_draw(0, 0, 1314, 394, bottom_image_x, 250 - 195)
    bottom_image.clip_draw(0, 0, 1314, 394, bottom_image_x_2, 250 - 195)
    mouse.clip_draw(0, 0, 73, 73, mouse_x, mouse_y)
    update_canvas()
    pass


def handle_events():
    global mouse_x, mouse_y
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, 500 - 1 - event.y - 73/2 + 3
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                game_framework.push_state(scene_main)
    pass


def pause():
    pass


def resume():
    pass