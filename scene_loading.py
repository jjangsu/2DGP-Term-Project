from pico2d import *
import game_framework
import scene_main
import cookie_bright
import cookie_brave
import scene_robby

image = None


def enter():
    global image, cookie
    if image == None:
        image = load_image('resource/background/LoadingBgOvenbreak.png')

    if scene_robby.select_cookie == 1:
        cookie = load_image('resource/character/One_Brave_Cookie.png')
    elif scene_robby.select_cookie == 2:
        cookie = load_image('resource/character/One_Bright_Cookie.png')
    pass


def exit():
    global image, cookie
    del (image)
    del (cookie)
    pass


def draw():
    global image, cookie
    image.clip_draw(0, 0, 1135, 799, 500, 250)
    cookie.clip_draw(0, 0, 300, 300, 500, 250, 80, 80)
    pass


def handle_events():
    pass

def pause():
    pass


def resume():
    pass