from pico2d import *
import game_framework
import scene_main
import cookie_bright
import cookie_brave
import scene_robby

image = None


def enter():
    global image, cookie, speed, previous_time

    if image == None:
        image = load_image('resource/background/LoadingBgOvenbreak.png')

    if scene_robby.select_cookie == 1:
        cookie = load_image('resource/character/One_Brave_Cookie.png')
    elif scene_robby.select_cookie == 2:
        cookie = load_image('resource/character/One_Bright_Cookie.png')

    speed = 500.0
    previous_time = get_time()
    pass


def exit():
    global image, cookie
    del (image)
    del (cookie)
    pass


def update():
    global previous_time, speed
    current = get_time()
    if current - previous_time >= 1.5:
        game_framework.change_state(scene_main)
pass


def draw():
    global image, cookie
    clear_canvas()
    image.clip_draw(0, 0, 1000, 703, 500, 250, 1000, 600)
    cookie.clip_draw(0, 0, 300, 300, 500, 180, 180, 180)
    update_canvas()
    pass


def handle_events():
    pass

def pause():
    pass


def resume():
    pass