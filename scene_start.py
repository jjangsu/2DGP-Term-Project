from pico2d import *
import game_framework
import scene_robby

image = None
start_time = 0.0
loading = None
loading_x = 0

def enter():
    global image, loading, loading_x
    hide_cursor()
    if image == None:
        image = load_image('resource/title.png')
    if loading == None:
        loading = load_image('resource/title_loading.png')
        loading_x = -1027/2
    pass

def exit():
    global image, loading
    del (image)
    del (loading)
    pass


def update():
    global start_time, loading_x
    if(start_time > 2.0):
        start_time = 0
        game_framework.change_state(scene_robby)
    start_time += 0.01
    loading_x += 1027 / 200
    pass


def draw():
    global image, loading
    clear_canvas()
    image.clip_draw(0, 0, 1027, 500, 500, 250)
    loading.clip_draw(0, 0, 1027, 16, loading_x, 8)
    update_canvas()
    pass


def handle_events():
    events = get_events()
    pass


def pause():
    pass


def resume():
    pass