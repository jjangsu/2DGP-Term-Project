from pico2d import *
import game_framework

PIXEL_PER_METER = (10.0 / 0.3)
RUN_SPEED_KMPH = 20.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 8

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

# character state


class RunningState:
    @staticmethod
    def enter(character, event):
        character.image_y = 4
        character.image_x = 0
        pass

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        # character.time += 1
        #if character.time > character.standard_time:
        character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % character.frame_num + character.image_x
        # character.time = 0

    @staticmethod
    def draw(character):
        character.image.clip_draw(int(character.frame) * 236, character.image_y * 236, 236, 236, character.x, character.y)
        pass


class JumpState:
    @staticmethod
    def enter(character, event):
        global direct, speed
       #  print(character.cur_state)
        # if event == L_SHIFT_DOWN:
        #     character.image_y = 0

        character.jump_timer = 200.0
        character.standard_time = 7.0
        character.frame = 0
        character.frame_num = 2
        character.image_y = 5
        character.image_x = 7
        direct = 1
        speed = 2.0
        pass

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        global direct, speed
        character.jump_timer -= 1.0
        if character.jump_timer <= 0.0:
            character.add_event(RUN_TIMER)
            character.y = 70 + 115

        character.y += direct * speed

        if character.y >= 172 + (70 + 115):
            direct = -1
            speed = 1.0

        character.time += 7.0
        if character.time > character.standard_time:
            character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % character.frame_num + character.image_x
            character.time = 0
            # print(character.frame_num)
        pass

    @staticmethod
    def draw(character):
        character.image.clip_draw(int(character.frame) * 236, character.image_y * 236, 236, 236, character.x, character.y)
        pass


class DoubleJumpState:
    @staticmethod
    def enter(character, event):
        global direct, speed
        character.standard_time = 7.0
        character.frame = 0
        character.frame_num = 7
        character.image_y = 5
        character.image_x = 0
        direct = 1
        speed = 2.0
        pass

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        global direct, speed

        character.jump_timer -= 1.0
        if character.jump_timer <= 0.0:
            character.add_event(RUN_TIMER)
            character.y = 70 + 115

        character.y += direct * speed

        if character.y >= 280 + (70 + 115):
            direct = -1
            speed = 2.5

        character.time += 7.0
        if character.time > character.standard_time:
            character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % character.frame_num + character.image_x
            character.time = 0
        pass

    @staticmethod
    def draw(character):
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
        character.slide_timer = 150.0
        pass

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        character.time += 7.0
        if character.time > character.standard_time:
            character.frame = (character.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % character.frame_num + character.image_x
            character.time = 0
        pass

    @staticmethod
    def draw(character):
        character.image.clip_draw(int(character.frame) * 236, character.image_y * 236, 236, 236, character.x, character.y)
        pass


next_state_table = {
    RunningState: {L_SHIFT_DOWN: JumpState, L_SHIFT_UP: JumpState, RUN_TIMER: RunningState,
                   R_SHIFT_DOWN: SlideState, R_SHIFT_UP: SlideState,
                   Z_DOWN: RunningState, Z_UP: RunningState},
    JumpState: {L_SHIFT_DOWN: RunningState, L_SHIFT_UP: RunningState, RUN_TIMER: RunningState,
                R_SHIFT_DOWN:JumpState, R_SHIFT_UP: JumpState,
                Z_DOWN: DoubleJumpState, Z_UP: DoubleJumpState},
    SlideState: {L_SHIFT_DOWN: SlideState, L_SHIFT_UP: SlideState, RUN_TIMER: RunningState,
                 R_SHIFT_DOWN: SlideState, R_SHIFT_UP: RunningState,
                 Z_DOWN: SlideState, Z_UP: SlideState},
    DoubleJumpState: {L_SHIFT_DOWN: DoubleJumpState, L_SHIFT_UP: DoubleJumpState, RUN_TIMER: RunningState,
                      R_SHIFT_DOWN: DoubleJumpState, R_SHIFT_UP:DoubleJumpState,
                      Z_DOWN: DoubleJumpState, Z_UP: DoubleJumpState}
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
        self.image = None # load_image('resource/Brave Cookie.png')
        self.event_que = []
        self.cur_state = RunningState
        self.cur_state.enter(self, None)
        self.jump_timer = 0
        self.slide_timer = 0
        pass

    # def newPosition(self, x, y):
    #     self.x = x
    #     self.y = y
    #     pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        # self.time += 1
        # if self.time > self.standard_time:
        self.cur_state.do(self)
        if len(self.event_que) > 0:
            event = self.event_que.pop()
            self.cur_state.exit(self, event)
            self.cur_state = next_state_table[self.cur_state][event]
            self.cur_state.enter(self, event)

        #     self.frame = (self.frame + 1) % self.frame_num + self.image_x
        #     self.time = 0
        pass

    def draw(self):
        self.cur_state.draw(self)
        # self.image.clip_draw(self.frame * 236, self.image_y * 236, 236, 236, self.x, self.y)
        pass

    def handle_event(self, event):
        if (event.type, event.key) in key_event_table:
            key_event = key_event_table[(event.type, event.key)]
            self.add_event(key_event)