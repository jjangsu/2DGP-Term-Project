from pico2d import *
import game_framework
import scene_main
import cookie_bright
import cookie_brave
import scene_loading
import numpy as np
import json

top_image = None
top_image_x = 500
top_image_x_2 = 500 + 1030
bottom_image = None
bottom_image_x = 500
bottom_image_x_2 = 500 + 1314
mouse = None
mouse_x , mouse_y = 0, 0
select = None
click_x, click_y = 0, 0
select_cookie = 0
select_image = None
select_x = - 200
select_y = 350

play_image = None
no_play_image = None

play = False
bgm = None
pick = None
font = None
coin = None
list = None
coin_image = None

def enter():
    global top_image, bottom_image, mouse, brave, bright, select_image, play_image, no_play_image, bgm, pick, coin
    global font, list, coin_image
    if top_image == None:
        top_image = load_image('resource/background/robby_top1.png')

    if bottom_image == None:
        bottom_image = load_image('resource/background/robby_bottom.png')

    if mouse == None:
        hide_cursor()
        mouse = load_image('resource/UI/mouse1.png')

    if select_image == None:
        select_image = load_image('resource/UI/epN01_tm11_jp2down.png')

    if play_image == None:
        play_image = load_image('resource/UI/play.png')

    if no_play_image == None:
        no_play_image = load_image('resource/UI/no play.png')

    brave = cookie_brave.Brave()
    brave.newPosition(500 - 150, 250)

    bright = cookie_bright.Bright()
    bright.newPosition(500 + 150, 250)

    if bgm == None:
        bgm = load_music('sound/Cookierun- Ovenbreak - OST - Trial Mode Main Lobby Theme - Extended 10 minutes.mp3')
        bgm.get_volume()
        # bgm.set_volume(80)
    bgm.repeat_play()

    if pick == None:
        pick = load_wav('sound/picking.wav')
        pick.set_volume(60)

    if font == None:
        font = load_font('font/Maplestory Bold.ttf', 30)

    if coin_image == None:
        coin_image = load_image('resource/Cookie Skill Effects and Jellies/jelly/silver coin.png')

    f = open('coin data.txt', 'r')
    coin = f.read()
    f.close()
    pass

def exit():
    global top_image, bottom_image, mouse, brave, bright, play_image, no_play_image, pick
    pass


def update():
    global top_image_x, top_image_x_2, bottom_image_x, bottom_image_x_2, brave, bright, select, mouse_x, mouse_y, select_cookie
    global select_x, play, click_x, click_y
    top_image_x -= 100 * game_framework.frame_time
    if top_image_x <= -515:
        top_image_x = 1000 + 515
    top_image_x_2 -= 100 * game_framework.frame_time
    if top_image_x_2 <= -515:
        top_image_x_2 = 1000 + 515

    bottom_image_x -= 200.0 * game_framework.frame_time
    if bottom_image_x < -657:
        bottom_image_x = 1000 + 1314/2
    bottom_image_x_2 -=  200.0 * game_framework.frame_time
    if bottom_image_x_2 < -657:
        bottom_image_x_2 = 1000 + 1314 / 2

    # if not (brave.image_x == 4 and brave.image_y == 4):
    if select_cookie == 1:
        brave.image_x = 4
        brave.image_y = 4
        brave.frame_num = 4
        brave.standard_time = 2.0

    elif (not select_cookie == 1) and mouse_x > brave.x - 30 and mouse_x < brave.x + 50 and \
            mouse_y > brave.y - 130 and mouse_y < brave.y + 10:
        brave.image_x = 0
        brave.image_y = 3
        brave.frame_num = 6
        brave.standard_time = 5.0
        if click_x > brave.x - 30 and click_x < brave.x + 50 and \
                click_y > brave.y - 50 and click_y < brave.y + 50:
            select_cookie = 1
            select_x = 500 - 140
    else:
        brave.image_x = 0
        brave.image_y = 4
        brave.frame_num = 4
        brave.standard_time = 3.5

    # if  not (bright.image_x == 4 and  bright.image_y == 4):
    if select_cookie == 2:
        bright.image_x = 4
        bright.image_y = 4
        bright.frame_num = 4
        bright.standard_time = 2.

    elif (not select_cookie == 2) and  mouse_x > bright.x - 30 and mouse_x < bright.x + 50 and \
            mouse_y > bright.y - 130 and mouse_y < bright.y + 10:
        bright.image_x = 0
        bright.image_y = 3
        bright.frame_num = 6
        bright.standard_time = 5.0
        if click_x > bright.x - 30 and click_x < bright.x + 50 and \
                click_y > bright.y - 50 and click_y < bright.y + 50:
            select_cookie = 2
            select_x = 500 + 150
    else:
        bright.image_x = 0
        bright.image_y = 4
        bright.frame_num = 4
        bright.standard_time = 3.5

    if select_cookie == 0:
        play = False
    else:
        play = True

    brave.update()
    bright.update()

    if (not select_cookie == -1) and 500 - 150 < click_x and click_x < 500 + 150 and \
        60 < 500 - click_y and 500 - click_y < 60 + 85:
            game_framework.change_state(scene_loading)
            bgm.stop()


    pass


def draw():
    global top_image, bottom_image, top_image_2, bottom_image_x_2, brave, bright,coin
    clear_canvas()
    top_image.clip_draw(0, 0, 1030, 246, top_image_x, 250 + 125)
    top_image.clip_draw(0, 0, 1030, 246, top_image_x_2, 250 + 125)
    bottom_image.clip_draw(0, 0, 1314, 394, bottom_image_x, 250 - 195)
    bottom_image.clip_draw(0, 0, 1314, 394, bottom_image_x_2, 250 - 195)
    brave.draw()
    bright.draw()
    #if select_x > 100:
    if select_cookie != -1:
        select_image.clip_draw(0, 0, 110, 179, select_x, select_y)

    if play == True:
        play_image.clip_draw(0, 0, 300, 85, 1000 // 2, 60)
    else:
        no_play_image.clip_draw(0, 0, 300, 85, 1000 // 2, 60)

    coin_image.clip_draw(0, 0, 50, 50, 380, 460, 30, 30)
    font.draw(400, 460, '%s' % coin, (255, 255, 0))


    mouse.clip_draw(0, 0, 73, 73, mouse_x, mouse_y)
    update_canvas()
    pass


def handle_events():
    global mouse_x, mouse_y, click_x, click_y, pick
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, 500 - 1 - event.y - 73/2 + 3
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                pick.play()
                click_x, click_y = event.x, event.y - 73 / 2 + 3
        # elif event.type == SDL_KEYDOWN:
        #     if event.key == SDLK_SPACE:
        #         game_framework.push_state(scene_main)
    pass


def pause():
    pass


def resume():
    pass