from pico2d import *
import game_framework
import path
import background
import numpy as np
import obstacle
import character
import character_brave
import character_bright
import scene_robby
import life
import game_world


obstacles = []

def enter():
    global backgrounds, paths, obstacles, line, obstacle_type, cookie, select_cookie, timer, life_image
    backgrounds = background.Background()
    paths = [path.Path(n) for n in range(10)]
    if scene_robby.select_cookie == 1:
        cookie = character_brave.Brave()
        cookie.newPosition(200, 70 + 115)

    elif scene_robby.select_cookie == 2:
        cookie = character_bright.Bright()
        cookie.newPosition(200, 70 + 115)

    line = [[0] * 12 for i in range(12)]
    with open('obstacleData.txt', 'r') as file:
        line = np.loadtxt('obstacleData.txt', delimiter=' ')
    row = 0
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
            row += 1
        row = 0
        col += 1

    life_image = life.LIFE()
    game_world.add_object(life_image, 2)

    game_world.add_object(backgrounds, 0)
    for i in paths:
        game_world.add_object(i, 0)
    game_world.add_object(cookie, 2)
    for obs in obstacles:
        game_world.add_object(obs, 1)

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
    global timer, cookie, obstacles
    timer += 1
    # if timer > 2:
    for game_object in game_world.all_objects():
        if game_object == cookie and timer > 0:
            game_object.update()
            timer = 0
        elif not game_object == cookie:
            game_object.update()
        #timer = 0

   # for obs in obstacles:
   #     if collide(cookie, obs):
   #         print("COLLISION")


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
