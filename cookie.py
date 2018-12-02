from pico2d import *
import game_framework
import scene_main


PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 9

# character event
L_SHIFT_DOWN, L_SHIFT_UP, RUN_TIMER, R_SHIFT_DOWN, R_SHIFT_UP, Z_DOWN, Z_UP = range(7)

key_event_table = {
    (SDL_KEYDOWN, SDLK_LSHIFT): L_SHIFT_DOWN,
    (SDL_KEYUP, SDLK_SPACE): L_SHIFT_UP,
    (SDL_KEYDOWN, SDLK_RSHIFT): R_SHIFT_DOWN,
    (SDL_KEYUP, SDLK_RSHIFT): R_SHIFT_UP,
    (SDL_KEYDOWN, SDLK_z): Z_DOWN,
    (SDL_KEYUP, SDLK_z): Z_UP
}

jump_hate = False

speed = 0.001
height = 40
origin_y = 0.0
is_jumping = False
stop = False
timer = 0

pi = 3.14
angle = 0
double_angle, double_radian = 0, 0
stop = False


class RunningState:
    @staticmethod
    def enter(character, event):
        character.image_y = 4
        character.image_x = 0

        character.frame = 0
        character.frame_num = 4
        character.crash_x1 = 0
        character.crash_x2 = 40
        character.crash_y2 = 0

        pass

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        global timer
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % character.frame_num + character.image_x

        if character.crash_animation == 1:
            character.image_y = 1
            character.image_x = 0
            character.frame = 0
            character.frame_num = 1
        if character.crash_animation > 0:
            timer += 1

        if character.die_animation == 1:
            character.image_y = 1
            character.image_x = 5
            character.frame = 0
            character.frame_num = 5
        if character.frame >= 9:
            character.frame = 9


        if timer > 60:
            character.crash_animation = 0
            character.image_y = 4
            character.image_x = 0
            character.frame = 0
            character.frame_num = 4
            timer = 0

    @staticmethod
    def draw(character):
        character.image.opacify(character.opacity)
        character.image.clip_draw(int(character.frame) * 236, character.image_y * 236, 236, 236, character.x, character.y)
        pass


class JumpState:
    @staticmethod
    def enter(character, event):
        global direct, speed, jump_hate, angle
        character.jump_timer = 200.0
        character.standard_time = 7.0
        character.frame = 0
        character.frame_num = 2
        character.image_y = 5
        character.image_x = 7
        direct = 1
        speed = 2.0
        character.crash_x1 = 0
        character.crash_x2 = 40
        character.crash_y2 = 0
        jump_hate = True

        angle = 0.0

        scene_main.button.jump_push = True
        character.jump_sound.play(1)
        character.jump_sound.set_volume(70)
        pass

    @staticmethod
    def exit(character, event):
        global jump_hate
        jump_hate = False
        scene_main.button.jump_push = False
        pass

    @staticmethod
    def do(character):
        global direct, angle, radian, pi, timer, stop
        radian = math.radians(angle)
        character.y = 175 * math.sin(radian * pi) + (75 + 115)
        if not stop:
            angle += 50 * game_framework.frame_time
        if radian > 1:
            angle = 0.0
            radian = 0
            if character.die_animation > 0:
                stop = True
            if character.die_animation == 0:
                character.add_event(RUN_TIMER)

        character.time += 7.0
        if character.time > character.standard_time:
            character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % character.frame_num + character.image_x
            character.time = 0
        if character.crash_animation > 0:
            timer += 1

        if character.crash_animation == 1:
            character.image_y = 1
            character.image_x = 0
            character.frame = 0
            character.frame_num = 1

        if character.die_animation == 1:
            character.image_y = 1
            character.image_x = 5
            character.frame = 0
            character.frame_num = 5
        if character.frame >= 9:
            character.frame = 9

        if timer > 60:
            character.crash_animation = 0
            character.frame = 0
            character.frame_num = 2
            character.image_y = 5
            character.image_x = 7
            timer = 0
        pass

    @staticmethod
    def draw(character):
        character.image.opacify(character.opacity)
        character.image.clip_draw(int(character.frame) * 236, character.image_y * 236, 236, 236, character.x, character.y)
        pass


class DoubleJumpState:
    @staticmethod
    def enter(character, event):
        global direct, speed, double_angle, origin_y, double_radian, height
        character.jump_timer = 150.0
        character.standard_time = 7.0
        character.frame = 0
        character.frame_num = 7
        character.image_y = 5
        character.image_x = 0
        direct = 1
        speed = 3.0
        character.crash_x1 = 0
        character.crash_x2 = 40
        character.crash_y2 = 0

        double_radian = 0.0
        double_angle = 0.0
        origin_y = character.y

        height = 100

        scene_main.button.jump_push = True
        scene_main.button.opacity_jump = 0.7

        character.Double_jump_sound.play(1)
        character.Double_jump_sound.set_volume(70)

        character.double_jump = True
        pass

    @staticmethod
    def exit(character, event):
        scene_main.button.jump_push = False
        scene_main.button.opacity_jump = 0.3
        character.double_jump = False
        pass

    @staticmethod
    def do(character):
        global direct, speed, double_angle, double_radian, origin_y, height, timer, stop
        double_radian = math.radians(double_angle)
        character.y = height * math.sin(double_radian * pi) + origin_y
        if character.y > 75 + 115:
            double_angle += 80 * game_framework.frame_time
            if character.die_animation > 0:
                stop = True
        if double_radian >= 1.0:
            height = 200
            origin_y -= 1.0

        if character.y < 75 + 115:
            character.y = 75 + 115
            if not stop:
                character.add_event(RUN_TIMER)

        character.time += 8.2
        if character.time > character.standard_time:
            character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % character.frame_num + character.image_x
            character.time = 0

        if character.crash_animation == 1:
            character.image_y = 1
            character.image_x = 0
            character.frame = 0
            character.frame_num = 1
        if character.crash_animation > 0:
            timer += 1

        if character.die_animation == 1:
            character.image_y = 1
            character.image_x = 5
            character.frame = 0
            character.frame_num = 5
        if character.frame >= 9:
            character.frame = 9

        if character.die_animation == 1:
            character.y = 75 + 115
            character.image_y = 1
            character.image_x = 5
            character.frame = 0
            character.frame_num = 5
        if character.frame >= 9:
            character.frame = 9

        if timer > 60:
            character.crash_animation = 0
            character.frame = 0
            character.frame_num = 7
            character.image_y = 5
            character.image_x = 0
            timer = 0
        pass

    @staticmethod
    def draw(character):
        character.image.opacify(character.opacity)
        character.image.clip_draw(int(character.frame) * 236, character.image_y * 236, 236, 236, character.x, character.y)
        pass


class SlideState:
    @staticmethod
    def enter(character, event):
        character.standard_time = 7.0
        character.frame = 0
        character.frame_num = 2
        character.image_y = 5
        character.image_x = 9

        character.crash_x1 = -40
        character.crash_x2 = 60
        character.crash_y2 = - 55

        scene_main.button.slide_push = True

        character.slide_sound.play(1)
        character.slide_sound.set_volume(70)
        pass

    @staticmethod
    def exit(character, event):
        scene_main.button.slide_push = False
        pass

    @staticmethod
    def do(character):
        global timer
        character.time += 7.0
        if character.time > character.standard_time:
            character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % character.frame_num + character.image_x
            character.time = 0

        if character.crash_animation == 1:
            character.image_y = 1
            character.image_x = 0
            character.frame = 0
            character.frame_num = 1
        if character.crash_animation > 0:
            timer += 1

        if character.die_animation == 1:
            character.image_y = 1
            character.image_x = 5
            character.frame = 0
            character.frame_num = 5
        if character.frame >= 9:
            character.frame = 9


        if timer > 60:
            character.crash_animation = 0
            character.frame = 0
            character.frame_num = 2
            character.image_y = 5
            character.image_x = 9
            timer = 0
        pass

    @staticmethod
    def draw(character):
        character.image.opacify(character.opacity)
        character.image.clip_draw(int(character.frame) * 236, character.image_y * 236, 236, 236, character.x, character.y)
        pass


next_state_table = {
    RunningState: {L_SHIFT_DOWN: JumpState, L_SHIFT_UP: JumpState, RUN_TIMER: RunningState,
                   R_SHIFT_DOWN: SlideState, R_SHIFT_UP: SlideState,
                   Z_DOWN: RunningState, Z_UP: RunningState,
                   },
    JumpState: {L_SHIFT_DOWN: JumpState, L_SHIFT_UP: RunningState, RUN_TIMER: RunningState,
                R_SHIFT_DOWN: JumpState, R_SHIFT_UP: JumpState,
                Z_DOWN: DoubleJumpState, Z_UP: DoubleJumpState,
                },
    SlideState: {L_SHIFT_DOWN: SlideState, L_SHIFT_UP: SlideState, RUN_TIMER: RunningState,
                 R_SHIFT_DOWN: SlideState, R_SHIFT_UP: RunningState,
                 Z_DOWN: SlideState, Z_UP: SlideState,
                 },
    DoubleJumpState: {L_SHIFT_DOWN: DoubleJumpState, L_SHIFT_UP: DoubleJumpState,
                      RUN_TIMER: RunningState,
                      R_SHIFT_DOWN: DoubleJumpState, R_SHIFT_UP: DoubleJumpState,
                      Z_DOWN: DoubleJumpState, Z_UP: DoubleJumpState,
                      },
}


class Character:
    def __init__(self):
        self.x = 200
        self.y = 70 + 115
        self.image_y = 4
        self.image_x = 0
        self.frame_num = 4
        self.frame = 0
        self.time = 0
        self.standard_time = 3.0
        self.image = None
        self.event_que = []
        self.cur_state = RunningState
        self.cur_state.enter(self, None)
        self.jump_timer = 0
        self.opacity = 1.0

        self.crash_x1 = 0
        self.crash_x2 = 40
        self.crash_y1 = 120
        self.crash_y2 = 0

        self.crash = False
        self.crash_timer = 0
        self.crash_num = 0

        self.score = 0
        self.coin = 0

        self.jump_sound = None
        self.Double_jump_sound = None
        self.slide_sound = None

        self.double_jump = False

        self.crash_animation = 0

        self.die_animation = 0

        self.sound_general = load_wav('sound/effect sound/g_jelly.wav')
        self.sound_general.set_volume(50)

        self.sound_gold_coin = load_wav('sound/effect sound/g_gold.wav')
        self.sound_gold_coin.set_volume(50)

        self.sound_silver_coin = load_wav('sound/effect sound/g_coin.wav')
        self.sound_silver_coin.set_volume(50)

        self.sound_bear = load_wav('sound/effect sound/g_alphabet.wav')
        self.sound_bear.set_volume(50)

        self.die_sound = load_wav('sound/g_end.wav')
        self.die_sound.set_volume(50)

        pass

    def add_event(self, event):
        if self.die_animation == 0:
            self.event_que.insert(0, event)

    def update(self):
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)
        pass

    def draw(self):
        if self.crash:
            self.opacity = 0.5
            self.crash_timer += 1
            if self.crash_timer > 130:
                self.opacity = 1.0
                self.crash = False
                self.crash_timer = 0
                self.crash_num = 0
        self.cur_state.draw(self)
        draw_rectangle(*self.get_bb())
        pass

    def handle_event(self, event):
        global jump_hate
        if not self.double_jump:
            if (event.type, event.key) in key_event_table:
                key_event = key_event_table[(event.type, event.key)]
                if not jump_hate:
                    self.add_event(key_event)
                if jump_hate and not self.double_jump:
                    if key_event == Z_DOWN:
                        self.add_event(key_event)
