from pico2d import *
import game_framework
import scene_main
import scene_robby


black = None
base = None
font = None
coin_image = None
jelly_image = None

def enter():
    global base, black, font, coin_image, jelly_image
    show_cursor()

    if base == None:
        base = load_image('resource/background/finish.png')

    if black == None:
        black = load_image('resource/background/black.png')

    if font == None:
        font = load_font('font/Maplestory Bold.ttf', 40)

    if coin_image == None:
        coin_image = load_image('resource/Cookie Skill Effects and Jellies/jelly/silver coin.png')
    if jelly_image == None:
        jelly_image = load_image('resource/Cookie Skill Effects and Jellies/jelly/simple jelly.png')

    tmp = scene_main.cookie.coin + int(scene_robby.coin)

    f = open('coin data.txt', 'w')
    f.write(str(tmp))
    f.close()
    pass


def exit():
    global base
    del base
    del black
    del font
    del coin_image
    del jelly_image
    pass

def update():
    pass

def draw():
    global base, black, font
    clear_canvas()
    black.clip_draw(0, 0, 1000, 500, 500, 250)
    base.clip_draw(0, 0, 1000, 500, 500, 250)
    font.draw(280, 350, '획득 점수', (150, 150, 150))
    jelly_image.clip_composite_draw(00, 0, 40, 57, 1.57 * 2, 'v', 255, 300, 30, 40)
    font.draw(275, 300, '%d' % scene_main.cookie.score, (255, 255, 0))
    font.draw(590, 350, '획득 코인', (150, 150, 150))
    coin_image.clip_draw(0, 0, 50, 50, 600, 300, 30, 30)
    font.draw(620, 300, '%d' % scene_main.cookie.coin, (255, 255, 0))
    update_canvas()
    pass

def handle_events():
    pass

def pause():
    pass

def resume():
    pass