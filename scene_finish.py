from pico2d import *
import game_framework
import scene_main
import scene_robby
import random

TIME_PER_ACTION = 0.4
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2

black = None
base = None
font = None
coin_image = None
jelly_image = None
best_score = None
cookie = None
cookie_frame = 0

class Particle:
    particle = None

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.timer = -1
        self.frame = 0

        if Particle.particle == None:
            Particle.particle = load_image('resource/UI/particle 2.png')
        pass

    def draw(self):
        # if self.timer <= 0:
        Particle.particle.clip_draw(256 * int(self.frame), 0, 256, 256, self.x, self.y, 80, 80)

        pass

    def update(self):
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        self.timer -= 1
        if self.timer < 0:
            self.timer = 120
        pass


def enter():
    global base, black, font, coin_image, jelly_image, particle, particles, best_score, cookie
    show_cursor()

    if base == None:
        base = load_image('resource/background/finish.png')

    if black == None:
        black = load_image('resource/background/black.png')

    if font == None:
        font = load_font('font/Maplestory Bold.ttf', 40)

    if coin_image == None:
        coin_image = load_image('resource/Cookie Skill Effects and Jellies/jelly/silver coin.png')
    if jelly_image == None:
        jelly_image = load_image('resource/Cookie Skill Effects and Jellies/jelly/simple jelly.png')

    tmp = scene_main.cookie.coin + int(scene_robby.coin)

    particles = [Particle(315, 450), Particle(685, 450)]

    file = open('score.txt', 'r')
    best_score = file.read()
    file.close()

    if scene_main.cookie.score > int(best_score):
        best_score = scene_main.cookie.score
        file = open('score.txt', 'w')
        file.write(str(best_score))
        file.close()

    f = open('coin data.txt', 'w')
    f.write(str(tmp))
    f.close()

    if scene_robby.select_cookie == 1:
        if cookie == None:
            cookie = load_image('resource/character/Brave cookie.png')
    elif scene_robby.select_cookie == 2:
        if cookie == None:
            cookie = load_image('resource/character/Bright cookie.png')
    pass


def exit():
    global base
    del base
    del black
    del font
    del coin_image
    del jelly_image
    pass

def update():
    global particles, cookie_frame
    cookie_frame = (cookie_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5 + 5
    for p in particles:
        p.update()
    pass

def draw():
    global base, black, font, particles, best_score, cookie, cookie_frame
    clear_canvas()
    black.clip_draw(0, 0, 1000, 500, 500, 250)
    base.clip_draw(0, 0, 1000, 500, 500, 250)
    font.draw(280, 350, 'SCORE', (200, 200, 200))
    jelly_image.clip_composite_draw(00, 0, 40, 57, 1.57 * 2, 'v', 255, 300, 30, 40)
    font.draw(275, 300, '%d' % scene_main.cookie.score, (255, 255, 0))
    font.draw(230, 250, 'BSET SCORE', (200, 200, 200))
    jelly_image.clip_composite_draw(00, 0, 40, 57, 1.57 * 2, 'v', 255, 200, 30, 40)
    font.draw(275, 200, '%s' % best_score, (255, 255, 255))
    font.draw(590, 350, 'COIN', (200, 200, 200))
    coin_image.clip_draw(0, 0, 50, 50, 600, 300, 30, 30)
    font.draw(620, 300, '%d' % scene_main.cookie.coin, (255, 255, 255))

    cookie.clip_draw(int(cookie_frame) * 236,  1 * 236, 236, 236, 630, 218, 100, 100)

    for p in particles:
        p.draw()
    update_canvas()
    pass

def handle_events():
    pass

def pause():
    pass

def resume():
    pass