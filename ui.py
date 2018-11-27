from pico2d import *

class UI:
    button = None
    button_push = None
    jump = None
    slide = None

    def __init__(self):
        self.opacity_jump = 0.3
        self.opacity_slide = 0.4
        self.jump_push = 0
        self.slide_push = False
        self.icon_opacity = 0.7
        self.double_jump_opacity = 0.9

        if UI.button == None:
            UI.button = load_image('resource/UI/button.png')

        if UI.button_push == None:
            UI.button_push = load_image('resource/UI/button push.png')

        if UI.jump == None:
            UI.jump = load_image('resource/UI/jump.png')

        if UI.slide == None:
            UI.slide = load_image('resource/UI/slide.png')

        pass

    def update(self):
        pass

    def draw(self):
        UI.button.opacify(self.opacity_jump)
        if self.jump_push == 0:
            UI.button.clip_draw(0, 0, 173, 131, 100, 80, 150, 110)
        else:
            UI.button_push.opacify(self.opacity_jump)
            UI.button_push.clip_draw(0, 0, 173, 131, 100, 80, 150, 110)

        UI.jump.opacify(self.icon_opacity)
        UI.jump.clip_draw(0, 0, 103, 42, 100, 80, 100, 40)

        UI.button.opacify(self.opacity_slide)
        if(self.slide_push == False):
            UI.button.clip_draw(0, 0, 173, 131, 900, 80, 150, 110)
        else:
            UI.button_push.opacify(self.opacity_jump)
            UI.button_push.clip_draw(0, 0, 173, 131, 900, 80, 150, 110)

        UI.slide.opacify(self.icon_opacity)
        UI.slide.clip_draw(0, 0, 103, 42, 900, 80, 100, 40)
        pass