from pico2d import *
import game_framework
import scene_main


black = None
base = None
font = None

def enter():
    global base, black, font
    show_cursor()

    if base == None:
        base = load_image('resource/background/finish.png')

    if black == None:
        black = load_image('resource/background/black.png')

    if font == None:
        font = load_font('font/Maplestory Bold.ttf', 40)
    pass


def exit():
    global base
    del base
    pass

def update():
    pass

def draw():
    global base, black, font
    clear_canvas()
    black.clip_draw(0, 0, 1000, 500, 500, 250)
    base.clip_draw(0, 0, 1000, 500, 500, 250)
    font.draw(280, 350, '획득 점수', (150, 150, 150))
    font.draw(275, 300, '%d' % scene_main.cookie.score, (255, 255, 0))
    font.draw(590, 350, '획득 코인', (150, 150, 150))
    font.draw(620, 300, '%d' % scene_main.cookie.coin, (255, 255, 0))
    update_canvas()
    pass

def handle_events():
    pass

def pause():
    pass

def resume():
    pass