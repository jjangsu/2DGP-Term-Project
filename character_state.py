from pico2d import *

UP_DOWN, UP_UP, DOWN_DOWN, DOWN_UP, SHIFT_DOWN, SHIFT_UP = range(6)

key_event_table = {
    (SDL_KEYDOWN, SDLK_UP): UP_DOWN,
    (SDL_KEYDOWN, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYDOWN, SDLK_RSHIFT): SHIFT_DOWN,
    (SDL_KEYUP, SDLK_UP): UP_UP,
    (SDL_KEYUP, SDLK_DOWN): DOWN_DOWN,
    (SDL_KEYUP, SDLK_RSHIFT): SHIFT_UP,
}

class RunState:

    @staticmethod
    def enter(Brave):
        pass

    @staticmethod
    def exit(Brave):
        pass

    @staticmethod
    def do(Brave):
        pass

    @staticmethod
    def draw(Brave):
        pass


class JumpState:

    @staticmethod
    def enter(Brave):
        pass

    @staticmethod
    def exit(Brave):
        pass

    @staticmethod
    def do(Brave):
        pass

    @staticmethod
    def draw(Brave):
        pass


class DoubleJumpState:

    @staticmethod
    def enter(Brave):
        pass

    @staticmethod
    def exit(Brave):
        pass

    @staticmethod
    def do(Brave):
        pass

    @staticmethod
    def draw(Brave):
        pass

