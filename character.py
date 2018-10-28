from pico2d import *

# character event
SPACE_DOWN, SPACE_UP = range(2)

key_event_table = {
    (SDL_KEYDOWN, SDLK_SPACE): SPACE_DOWN,
    (SDL_KEYUP, SDLK_SPACE): SPACE_UP
}

# character state


class RunningState:
    @staticmethod
    def enter(character, event):
        if event == SPACE_DOWN:
            character.jump += 1
        elif event == SPACE_UP:
            character.jump -= 1
        pass

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        character.time += 1
        if character.time > character.standard_time:
            character.frame = (character.frame + 1) % character.frame_num + character.image_x
            character.time = 0
        pass
#
    @staticmethod
    def draw(character):
        character.image.clip_draw(character.frame * 236, character.image_y * 236, 236, 236, character.x, character.y)
        pass


class JumpState:
    @staticmethod
    def enter(character, event):
        pass

    @staticmethod
    def exit(character, event):
        pass

    @staticmethod
    def do(character):
        pass

    @staticmethod
    def draw(character):
        pass

next_state_table ={
    RunningState: {SPACE_DOWN: JumpState, SPACE_UP: JumpState},
    JumpState: {SPACE_DOWN: RunningState, SPACE_UP: RunningState}
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
        self.jump = 0
        self.event_que = []
        self.cur_state = RunningState
        self.cur_state.enter(self, None)
        pass

    # def newPosition(self, x, y):
    #     self.x = x
    #     self.y = y
    #     pass

    def add_event(self, event):
        self.event_que.insert(0, event)

    def update(self):
        self.time += 1
        if self.time > self.standard_time:
            self.cur_state.do(self)
            if len(self.event_que) > 0:
                event = self.event_que.pop()
                self.cur_state.exit(self, event)
                self.cur_state = next_state_table[self.cur_state][event]
                self.cur_state.enter(self, event)
        #
        #
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