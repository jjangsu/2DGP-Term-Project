from pico2d import *
import game_framework
import scene_robby

image = None
start_time = 0.0

def enter():
    global image
    if image == None:
        image = load_image('resource/title.png')
    pass

def exit():
    global image
    del (image)
    pass


def update():
    global start_time
    if(start_time > 2.0):
        start_time = 0
        game_framework.change_state(scene_robby)
    start_time += 0.01
    pass


def draw():
    global image
    clear_canvas()
    image.clip_draw(0, 0, 1027, 500, 500, 250)
    update_canvas()
    pass


def handle_events():
    events = get_events()
    pass


def pause():
    pass


def resume():
    pass