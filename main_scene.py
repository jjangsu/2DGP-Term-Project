from pico2d import *
import game_framework
import path
import background
import numpy as np
import obstacle

obstacles = []

def enter():
    global backgrounds, paths, obstacles, line
    backgrounds = background.Background()
    paths = [path.Path(n) for n in range(10)]

    line = [[0] * 3 for i in range(10 + 1)]
    with open('obstacle.txt', 'r') as file:
        line = np.loadtxt('obstacle.txt', delimiter=' ')
    t = 1
    for i in line:
        for j in i:
            j = int(j)
            if j == 1:
                obstacle_type = 1
            if j != 0:
                obstacles.append(obstacle.Obstacle(obstacle_type, t))
            t = t + 1
                #obstacles = [obstacle.Obstacle(obstacle_type, n) for n in i]
    pass
#

def exit():
    global backgrounds, paths, obstacles
    del (backgrounds)
    del (paths)
    del(obstacles)
    pass


def update():
    global backgrounds, paths, obstacles
    backgrounds.update()
    for path in paths:
        path.update()
    for obstacle in obstacles:
        obstacle.update()
    pass


def draw():
    global backgrounds, paths, obstacles
    clear_canvas()
    backgrounds.draw()
    for path in paths:
        path.draw()
    for obstacle in obstacles:
        obstacle.draw()
    update_canvas()
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
    pass


def pause():
    pass


def resume():
    pass
