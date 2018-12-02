from pico2d import *
import game_framework
import scene_main
import scene_lobby
import game_world

TIME_PER_ACTION = 0.4
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 2

black = None
base = None
font = None
small_font = None
coin_image = None
jelly_image = None
best_score = None
cookie = None
cookie_frame = 0
mouse = None
mouse_x, mouse_y = 0, 0
main = None
click_x, click_y = 0, 0
sound = None

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
    global base, black, font, coin_image, jelly_image, particle, particles, best_score, cookie, mouse, main, small_font, sound
    global click_x, click_y
    click_x, click_y = 0, 0
    if mouse == None:
        hide_cursor()
        mouse = load_image('resource/UI/mouse1.png')

    if base == None:
        base = load_image('resource/background/finish.png')

    if black == None:
        black = load_image('resource/background/black.png')

    if font == None:
        font = load_font('font/Maplestory Bold.ttf', 40)

    if small_font == None:
        small_font = load_font('font/Maplestory Bold.ttf', 20)

    if coin_image == None:
        coin_image = load_image('resource/Cookie Skill Effects and Jellies/jelly/silver coin.png')
    if jelly_image == None:
        jelly_image = load_image('resource/Cookie Skill Effects and Jellies/jelly/simple jelly.png')

    tmp = scene_main.cookie.coin + int(scene_lobby.coin)

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

    if scene_lobby.select_cookie == 1:
        if cookie == None:
            cookie = load_image('resource/character/Brave cookie.png')
    elif scene_lobby.select_cookie == 2:
        if cookie == None:
            cookie = load_image('resource/character/Bright cookie.png')

    if main == None:
        main = load_image('resource/UI/oven.png')

    if sound == None:
        sound = load_wav('sound/effect sound/r_medal.wav')
    sound.get_volume()
    sound.play(1)
    pass


def exit():
    global base, black, font, coin_image, jelly_image, particles, best_score, cookie, mouse, main, small_font
    scene_main.jellies.clear()
    scene_main.obstacles.clear()
    pass


def update():
    global particles, cookie_frame, click_x, click_x

    cookie_frame = (cookie_frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5 + 5
    for p in particles:
        p.update()

    if 450 < click_x and click_x < 500 and \
        20 < 500 - click_y and 500 - click_y < 100:
        scene_lobby.select_cookie = -1
        scene_lobby.play = False
        game_world.clear()
        game_framework.change_state(scene_lobby)
    pass


def draw():
    global base, black, font, particles, best_score, cookie, cookie_frame
    clear_canvas()
    black.clip_draw(0, 0, 1000, 500, 500, 250)
    base.clip_draw(0, 0, 1000, 500, 500, 250)
    font.draw(280, 380, 'SCORE', (200, 200, 200))
    jelly_image.clip_composite_draw(00, 0, 40, 57, 1.57 * 2, 'v', 255, 330, 30, 40)
    font.draw(275, 330, '%d' % scene_main.cookie.score, (255, 255, 0))
    font.draw(230, 250, 'BSET SCORE', (200, 200, 200))
    jelly_image.clip_composite_draw(00, 0, 40, 57, 1.57 * 2, 'v', 255, 200, 30, 40)
    font.draw(275, 200, '%s' % best_score, (255, 255, 255))
    font.draw(590, 380, 'COIN', (200, 200, 200))
    coin_image.clip_draw(0, 0, 50, 50, 600, 330, 30, 30)
    font.draw(620, 330, '%d' % scene_main.cookie.coin, (255, 255, 255))

    cookie.clip_draw(int(cookie_frame) * 236,  1 * 236, 236, 236, 630, 265, 200, 200)

    main.clip_draw(0, 0, 340, 296, 470, 50, 80, 69)
    small_font.draw(520, 55, '메인으로', (250, 250, 100))
    small_font.draw(520, 35, '돌아가기', (250, 250, 100))

    mouse.clip_draw(0, 0, 73, 73, mouse_x, mouse_y)

    for p in particles:
        p.draw()
    update_canvas()
    pass


def handle_events():
    global mouse_x, mouse_y, click_y, click_x
    events = get_events()
    for event in events:
        if event.type == SDL_MOUSEMOTION:
            mouse_x, mouse_y = event.x, 500 - 1 - event.y - 73 / 2 + 3
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                click_x, click_y = event.x, event.y - 73 / 2 + 3
    pass


def pause():
    pass


def resume():
    pass

