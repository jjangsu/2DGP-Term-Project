from pico2d import *
import game_framework
import path
import background
import obstacle

def enter():
    global backgrounds, paths, obstacle
    backgrounds = background.Background()
    paths = [path.Path(n) for n in range(10)]
    obstacle = obstacle.Obstacle()
    pass


def exit():
    global backgrounds, paths, obstacle
    del (backgrounds)
    del (paths)
    del(obstacle)
    pass


def update():
    global backgrounds, paths, obstacle
    backgrounds.update()
    for path in paths:
        path.update()
    obstacle.update()
    pass


def draw():
    global backgrounds, paths
    clear_canvas()
    backgrounds.draw()
    for path in paths:
        path.draw()
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
