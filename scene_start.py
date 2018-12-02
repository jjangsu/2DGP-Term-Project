from pico2d import *
import game_framework
import scene_lobby

image = None
start_time = 0.0
loading = None
loading_x = 0
bgm = None

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 54.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

def enter():
    global image, loading, loading_x, previous_time, speed, bgm
    hide_cursor()
    if image == None:
        image = load_image('resource/background/title.png')
    if loading == None:
        loading = load_image('resource/UI/title_loading.png')

    bgm = load_music('sound/loading sound - cutting2.mp3')
    bgm.get_volume()
    bgm.repeat_play()
    loading_x = - 512.0 # (1027.0 / 2.0)
    # print(loading_x)
    speed = 400.0

    previous_time = get_time()
    pass

def exit():
    global image, loading, bgm
    del(bgm)
    del (image)
    del (loading)

    pass


def update():
    global start_time, loading_x, previous_time, speed
    loading_x += speed * game_framework.frame_time # 1027 / 470
    current = get_time()
    if current - previous_time >= 2.5:
        game_framework.change_state(scene_lobby)
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