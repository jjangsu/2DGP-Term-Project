from pico2d import *
import game_framework
import path
import background

def enter():
    global backgrounds, paths
    backgrounds = background.Background()
    paths = [path.Path(n) for n in range(10)]
    pass


def exit():
    global backgrounds, paths
    del (backgrounds)
    del (paths)
    pass


def update():
    global backgrounds, paths
    backgrounds.update()
    for path in paths:
        path.update()
    pass


def draw():
    global backgrounds, paths
    clear_canvas()
    backgrounds.draw()
    for path in paths:
        path.draw()
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
