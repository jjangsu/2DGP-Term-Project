from pico2d import *
import game_framework
import path
import background
import numpy as np
import cookie_brave
import cookie_bright
import scene_robby
import life
import game_world
import obstacle_pin_bean
import obstacle_fork_sky
import obstacle_fork_sausage
import obstacle_fly_stone_1
import obstacle_fly_stone_4
import obstacle_trident
import jelly_general
import threading
import jelly_gold_coin
import jelly_silver_coin
import jelly_pink_bear
import jelly_yellow_bear


obstacles = []
jellies = []

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
    global backgrounds, paths, obstacles, line, cookie, select_cookie, timer, life_image, jelly_line, jelly_file
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

    paths = [path.Path(n) for n in range(10)]
    for i in paths:
        game_world.add_object(i, 0)
#
    life_image = life.LIFE()
    game_world.add_object(life_image, 2)

    timer = 0


def exit():
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
    global timer, cookie, obstacles, life_image, fps
    timer += 1
    # if timer > 2:
    fps = game_framework.frame_time

    for game_object in game_world.all_objects():
        if game_object == cookie and timer > 0:
            game_object.update()
            timer = 0
        elif not game_object == cookie:
            game_object.update()

    for obs in obstacles:
        if collide(cookie, obs):
            # print("COLLISION")
            cookie.crash = True
            cookie.crash_num += 1
            if cookie.crash_num == 1:
                life_image.image_x += 40
            pass

    for obs in obstacles:
        if obs.x < - 50:
            game_world.remove_object(obs)

    for item in jellies:
        if collide(cookie, item):
            game_world.remove_object(item)
        elif item.x < -10:
            game_world.remove_object(item)


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
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
