from pico2d import *
import game_framework
import path
import background
import numpy as np
import cookie_brave
import cookie_bright
import scene_robby
import scene_finish
import game_world
import obstacle_pin_bean
import obstacle_fork_sky
import obstacle_fork_sausage
import obstacle_fly_stone_1
import obstacle_fly_stone_4
import obstacle_trident
import jelly_general
import jelly_gold_coin
import jelly_silver_coin
import jelly_pink_bear
import jelly_yellow_bear
import ui


obstacles = []
jellies = []
cookie = None
button = None
score = 0
score_font = None
count = 0
coin_image = None
jelly_image = None
obs_sound = None


def jelly_init():
    jelly_line = [[0] * 5 for i in range(500)]
    with open('jellyData.txt', 'r') as jelly_file:
        jelly_line = np.loadtxt('jellyData.txt', delimiter=' ')
    row = 0
    col = 0
    for i in jelly_line:
        for j in i:
            j = int(j)
            if j == 1:
                jellies.append(jelly_general.General(row, col))
            elif j == 2:
                jellies.append(jelly_gold_coin.GoldCoin(row, col))
            elif j == 3:
                jellies.append(jelly_silver_coin.SilverCoin(row, col))
            elif j == 4:
                jellies.append(jelly_pink_bear.PinkBear(row, col))
            elif j == 5:
                jellies.append(jelly_yellow_bear.YellowBear(row, col))
                # print(row)
            row += 1
        row = 0
        col += 1


def obstacle_init():
    line = [[0] * 12 for i in range(24)]
    with open('obstacleData.txt', 'r') as file:
        line = np.loadtxt('obstacleData.txt', delimiter=' ')
    row = 0
    col = 0
    for i in line:
        for j in i:
            j = int(j)
            if j == 1:
                obstacles.append(obstacle_pin_bean.Pin_bean(row, col))
            elif j == 2:
                obstacles.append(obstacle_fork_sausage.Fork_sausage(row, col))
            elif j == 3:
                obstacles.append(obstacle_fork_sky.Fork_sky(row, col))
            elif j == 4:
                obstacles.append(obstacle_fly_stone_1.Stone_1(row, col))
            elif j == 5:
                obstacles.append(obstacle_fly_stone_4.Stone_4(row, col))
            elif j == 6:
                obstacles.append(obstacle_trident.Trident(row, col))
            row += 1
        row = 0
        col += 1
    for obs in obstacles:
        game_world.add_object(obs, 1)


def enter():
    global backgrounds, paths, obstacles, line, cookie, select_cookie, timer, jelly_line, jelly_file
    global button, score_font, score_font_back, coin_image, jelly_image, obs_sound

    backgrounds = background.Background()
    game_world.add_object(backgrounds, 0)

    if scene_robby.select_cookie == 1:
        cookie = cookie_brave.Brave()
        cookie.newPosition(200, 70 + 115)
    elif scene_robby.select_cookie == 2:
        cookie = cookie_bright.Bright()
        cookie.newPosition(200, 70 + 115)
    game_world.add_object(cookie, 2)

    obstacle_init()

    jelly_init()

    for item in jellies:
        game_world.add_object(item, 1)
        item.initialize()

    paths = [path.Path(n) for n in range(2)]
    for i in paths:
        game_world.add_object(i, 0)

    game_world.add_object(scene_robby.life_num, 2)

    timer = 0

    scene_robby.bgm = load_music('sound/Cookie Run Ovenbreak - Theme Song Breakout 1.mp3')
    scene_robby.bgm.get_volume()
    scene_robby.bgm.repeat_play()

    button = ui.UI()
    game_world.add_object(button, 2)

    if score_font == None:
        score_font = load_font('font/Maplestory Light.ttf', 20)

    if coin_image == None:
        coin_image = load_image('resource/Cookie Skill Effects and Jellies/jelly/silver coin.png')
    if jelly_image == None:
        jelly_image = load_image('resource/Cookie Skill Effects and Jellies/jelly/simple jelly.png')

    if obs_sound == None:
        obs_sound = load_wav('sound/effect sound/g_obs1.wav')
    obs_sound.set_volume(60)

    cookie.score = 0


def exit():
    global jellies, obstacles
    game_world.clear()


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()
    if left_a > right_b: return False
    if right_a < left_b: return False
    if top_a < bottom_b: return False
    if bottom_a > top_b: return False
    return True


def update():
    global timer, cookie, obstacles, fps, score, count, obs_sound
    timer += 1
    fps = game_framework.frame_time

    for game_object in game_world.all_objects():
        if game_object == cookie and timer > 0:
            game_object.update()
            timer = 0
        elif not game_object == cookie:
            game_object.update()

    if scene_robby.life_num.image_x > scene_robby.life_num.life_amount:
        scene_robby.bgm.stop()
        cookie.crash_animation = 0
        cookie.die_animation += 1
        cookie.crash = False
        if cookie.die_animation > 100:
            game_framework.change_state(scene_finish)

    for obs in obstacles:
        if collide(cookie, obs):
            cookie.crash = True
            cookie.crash_num += 1
            if cookie.die_animation == 0:
                cookie.crash_animation += 1
            if cookie.crash_animation == 1:
                obs_sound.play(1)
            if cookie.crash_num == 1:
                scene_robby.life_num.image_x += 40
            pass
        pass

    for obs in obstacles:
        if obs.x < - 50:
            game_world.remove_object(obs)


    for item in jellies:
        if collide(item, cookie):
            game_world.remove_object(item)
            jellies.remove(item)

            if item.type == 1:
                cookie.sound_general.play(1)
                cookie.score += 1500
            elif item.type == 2: # 골드코인
                cookie.sound_gold_coin.play(1)
                cookie.score += 800
                cookie.coin += 5
            elif item.type == 3: # 실버 코인
                cookie.sound_silver_coin.play(1)
                cookie.score += 500
                cookie.coin += 1
            elif item.type == 4: # 노란 곰
                cookie.sound_bear.play(1)
                cookie.score += 1800
            elif item.type == 5:
                cookie.sound_bear.play(1)
                cookie.score += 2000

        elif item.x < -10:
            game_world.remove_object(item)


def draw():
    global count
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    coin_image.clip_draw(0, 0, 50, 50, 40, 420, 30, 30)
    score_font.draw(60, 420, '%d' % cookie.coin, (255, 255, 100))
    score_font.draw(900, 435, 'SCORE', (255, 255, 0))
    jelly_image.clip_composite_draw(00, 0, 40, 57, 1.57 * 2, 'v', 870, 410, 20, 30)
    score_font.draw(890, 410, '%d' % cookie.score, (255, 255, 0))
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            cookie.handle_event(event)


def pause():
    pass


def resume():
    pass
