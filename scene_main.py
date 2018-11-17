from pico2d import *
import game_framework
import path
import background
import numpy as np
import obstacle
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
import jelly


obstacles = []
jellies = []

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
            # if j != 0:
            #     obstacles.append(obstacle.Obstacle(obstacle_type, row, col))
            row += 1
        row = 0
        col += 1
    for obs in obstacles:
        game_world.add_object(obs, 1)

    jelly_line = [[0] * 10 for i in range(1000)]
    with open('jellyData.txt', 'r') as jelly_file:
        jelly_line = np.loadtxt('jellyData.txt', delimiter=' ')
    row = 0
    col = 0
    for i in jelly_line:
        for j in i:
            j = int(j)
            if j == 1:
                jellies.append(jelly_general.General(row, col))

            row += 1
        row = 0
        col += 1
    for item in jellies:
        game_world.add_object(item, 1)
        item.initialize()
        # for obs in obstacles:
        #     if item.collide_obstacle(obs):
        #         item.newPosition(obs)

    paths = [path.Path(n) for n in range(10)]
    for i in paths:
        game_world.add_object(i, 0)

    # for j in jellies:
    #    print(j.y)

    life_image = life.LIFE()
    game_world.add_object(life_image, 2)

    # jellies = jelly_general.General()
    # jellies.initialize()
    # game_world.add_object(jellies, 1)
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
    global timer, cookie, obstacles, life_image
    timer += 1
    # if timer > 2:
    for game_object in game_world.all_objects():
        if game_object == cookie and timer > 0:
            game_object.update()
            timer = 0
        elif not game_object == cookie:
            game_object.update()
        #timer = 0

    for obs in obstacles:
        if collide(cookie, obs):
            # print("COLLISION")
            cookie.crash = True
            cookie.crash_num += 1
            if cookie.crash_num == 1:
                life_image.image_x += 30
            pass

    # for obs in obstacles:
    #     if obs.x < 0:
    #         game_world.remove_object(obs)
    # for item in jellies:
    #     if collide(cookie, item):
    #         game_world.remove_object(item)


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
