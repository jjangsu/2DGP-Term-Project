from pico2d import *
import game_framework
import path
import background
import numpy as np
import obstacle
import fps
import character_brave
import character_bright
import scene_robby

import game_world


obstacles = []

def enter():
    global backgrounds, paths, obstacles, line, obstacle_type, cookie, FPS, select_cookie
    FPS = fps.FPS()
    backgrounds = background.Background()
    paths = [path.Path(n) for n in range(10)]
    if scene_robby.select_cookie == 1:
        cookie = character_brave.Brave() # character_brave.Brave()#
        cookie.newPosition(200, 70 + 115)
    elif scene_robby.select_cookie == 2:
        cookie = character_bright.Bright()
        cookie.newPosition(200, 70 + 115)

    line = [[0] * 12 for i in range(12)]
    with open('obstacle.txt', 'r') as file:
        line = np.loadtxt('obstacle.txt', delimiter=' ')
    row = 1
    col = 0
    for i in line:
        for j in i:
            j = int(j)
            if j == 1:
                obstacle_type = 1
            elif j == 2:
                obstacle_type = 2
            elif j == 3:
                obstacle_type = 3
            elif j == 4:
                obstacle_type = 4
            if j != 0:
                obstacles.append(obstacle.Obstacle(obstacle_type, row, col))
            row = row + 1
        row = 4
        col += 1

        game_world.add_object(backgrounds, 0)
        for i in paths:
            game_world.add_object(i, 0)
        game_world.add_object(cookie, 2)
        for obs in obstacles:
            game_world.add_object(obs, 1)

#
def exit():
    # global backgrounds, paths, obstacles, cookie, FPS
    # del (backgrounds)
    # del (paths)
    # del (obstacles)
    # del (cookie)
    # del (FPS)#
    game_world.clear()


def update():
    # global backgrounds, paths, obstacles, cookie, FPS
    # FPS.update()
    # backgrounds.update()
    # for path in paths:
    #     path.update()
    # for obstacle in obstacles:
    #     obstacle.update()
    # cookie.update()
    for game_object in game_world.all_objects():
        game_object.update()


def draw():
    # global backgrounds, paths, obstacles, cookie
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()
    # backgrounds.draw()
    # for path in paths:#
    #     path.draw()
    # for obstacle in obstacles:
    #     obstacle.draw()
    # cookie.draw()
    update_canvas()


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()


def pause():
    pass


def resume():
    pass
