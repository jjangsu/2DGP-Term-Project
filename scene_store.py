from pico2d import *
import scene_main
import game_framework
import scene_lobby


back_image = None
all = None
font = None
blue = None
life = None
mouse = None
mouse_x , mouse_y = 0, 0
click_x, click_y = 0, 0
coin_image = None
check = 0
main = None
small_font = None
pick = None
bgm = None


def enter():
    global back_image, all, font, blue, life, mouse, coin_image, check, main, small_font, click_x, click_y, pick, bgm
    click_y = 0
    click_x = 0
    if back_image == None:
        back_image = load_image('resource/background/store.png')
    if all == None:
        all = load_image('resource/UI/all.png')

    if blue == None:
        blue = load_image('resource/background/store item.png')

    if font == None:
        font = load_font('font/Maplestory Bold.ttf', 40)

    if small_font == None:
        small_font = load_font('font/Maplestory Bold.ttf', 20)

    if life == None:
        life = load_image('resource/UI/life.png')

    if mouse == None:
        hide_cursor()
        mouse = load_image('resource/UI/mouse1.png')

    if coin_image == None:
        coin_image = load_image('resource/Cookie Skill Effects and Jellies/jelly/silver coin.png')

    check = 0

    if main == None:
        main = load_image('resource/UI/oven.png')

    if pick == None:
        pick = load_wav('sound/picking.wav')
        pick.set_volume(60)

    #if bgm == None:
    bgm = load_wav('sound/effect sound/bgm_lobby.wav')
    bgm.get_volume()
    bgm.repeat_play()
    pass


def exit():
    pass


def update():
    global mouse_x, mouse_y, click_x, click_y, check, bgm
    if 150 - 100 < click_x and click_x < 150 + 100 and \
        80 < 500 - click_y and 500 - click_y < 380:
        check += 1
    elif 700 - 20 < click_x and click_x < 700 + 40 and \
            20 < 500 - click_y and 500 - click_y < 100:
        game_framework.change_state(scene_lobby)
        del bgm
    else:
        check = 0
    if check == 1 and int(scene_lobby.coin) >= 1000:
        click_x = 0
        click_y = 0
        tmp = int(scene_lobby.life_num.life_amount) + 10
        f = open('life data.txt', 'w')
        f.write(str(tmp))
        f.close()
        f = open('life data.txt', 'r')
        scene_lobby.life_num.life_amount = f.read()
        f.close()

        tmp = int(scene_lobby.coin) - 1000
        f = open('coin data.txt', 'w')
        f.write(str(tmp))
        f.close()
        f = open('coin data.txt', 'r')
        scene_lobby.coin = f.read()
        f.close()


    pass


def draw():
    global mouse_x, mouse_y, click_x, click_y, check
    clear_canvas()
    back_image.draw(500, 250)
    all.clip_composite_draw(0, 0, 275, 185, 1.57 * 2, 'v', 750, 250, 200, 142)
    blue.opacify(0.7)
    blue.draw(150, 200)
    blue.opacify(0.5)
    blue.draw(430, 200)
    life.clip_draw(0, 0, 88, 101, 110, 230, 120, 109)
    font.draw(160, 220, '+ 10', (255, 255, 0))
    font.draw(70, 150, '$ 1,000', (255, 255, 0))
    font.draw(70, 100, '생명 사기', (255, 255, 0))
    font.draw(350, 230, 'coming', (255, 255, 0))
    font.draw(370, 180, 'soon', (255, 255, 0))

    coin_image.clip_draw(0, 0, 50, 50, 340, 460, 30, 30)
    font.draw(360, 460, '%s' % scene_lobby.coin, (255, 255, 0))

    life.clip_draw(0, 0, 88, 101, 560, 460, 40, 45)
    font.draw(580, 460, '%s' % scene_lobby.life_num.life_amount, (255, 255, 0))

    main.clip_draw(0, 0, 340, 296, 700, 50, 80, 69)
    small_font.draw(750, 55, '메인으로', (250, 250, 100))
    small_font.draw(750, 35, '돌아가기', (250, 250, 100))

    mouse.clip_draw(0, 0, 73, 73, mouse_x, mouse_y)
    update_canvas()
    pass


def handle_events():
    global mouse_x, mouse_y, click_x, click_y
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, 500 - 1 - event.y - 73 / 2 + 3
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                pick.play()
                click_x, click_y = event.x, event.y - 73 / 2 + 3
    pass


def pause():
    pass


def resume():
    pass

