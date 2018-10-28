from pico2d import *
import game_framework
import fps
import scene_main
import character_bright
import character_brave

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
select_cookie = 1


def enter():
    global top_image, bottom_image, mouse, brave, bright
    if top_image == None:
        top_image = load_image('resource/robby_top1.png')

    if bottom_image == None:
        bottom_image = load_image('resource/robby_bottom.png')

    if mouse == None:
        hide_cursor()
        mouse = load_image('resource/mouse1.png')

    brave = character_brave.Brave()
    brave.newPosition(500 - 150, 250)

    bright = character_bright.Bright()
    bright.newPosition(500 + 150, 250)
    pass

def exit():
    global top_image, bottom_image, mouse, brave, bright
    del (top_image)
    del (bottom_image)
    del (mouse)
    del (brave)
    del (bright)
    pass


def update():
    global top_image_x, top_image_x_2, bottom_image_x, bottom_image_x_2, brave, bright, select, mouse_x, mouse_y
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

    if mouse_x > brave.x - 30 and mouse_x < brave.x + 50 and \
            mouse_y > brave.y - 130 and mouse_y < brave.y + 10:
        brave.image_y = 3
        brave.frame_num = 6
        brave.standard_time = 5.0

    else:
        brave.image_y = 4
        brave.frame_num = 4
        brave.standard_time = 3.5

    # if click_x > brave.x - 30 and click_x < brave.x + 50 and \
    #         click_y > brave.y - 50 and click_y < brave.y + 50:
    #     brave.image_x = 4
    #     brave.standard_time = 2.0
    # else:
    #     brave.image_x = 1


    if mouse_x > bright.x - 30 and mouse_x < bright.x + 50 and \
            mouse_y > bright.y - 130 and mouse_y < bright.y + 10:
        bright.image_y = 3
        bright.frame_num = 6
        bright.standard_time = 5.0
    else:
        bright.image_y = 4
        bright.frame_num = 4
        bright.standard_time = 3.5

    brave.update()
    bright.update()

    pass


def draw():
    global top_image, bottom_image, top_image_2, bottom_image_x_2, brave, bright
    clear_canvas()
    top_image.clip_draw(0, 0, 1030, 246, top_image_x, 250 + 125)
    top_image.clip_draw(0, 0, 1030, 246, top_image_x_2, 250 + 125)
    bottom_image.clip_draw(0, 0, 1314, 394, bottom_image_x, 250 - 195)
    bottom_image.clip_draw(0, 0, 1314, 394, bottom_image_x_2, 250 - 195)
    brave.draw()
    bright.draw()
    mouse.clip_draw(0, 0, 73, 73, mouse_x, mouse_y)
    update_canvas()
    pass


def handle_events():
    global mouse_x, mouse_y, click_x, click_y
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, 500 - 1 - event.y - 73/2 + 3
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                click_x, click_y = event.x, event.y - 73 / 2 + 3
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_SPACE:
                game_framework.push_state(scene_main)
    pass


def pause():
    pass


def resume():
    pass