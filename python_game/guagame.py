import pygame
from pygame.locals import *

class GuaGame(object):
    def __init__(self, level=1):
        self.game = pygame
        self.screen = pygame.display.set_mode((800,600))
        self.actions = {}
        self.paused = False
        self.level = level
        self.pick_level = False

    def set_background(self):
        self.screen.fill([255,255,255])
    
    def init_pygame(self):
        self.game.init()
        self.game.display.set_caption("撞砖块")
        self.game.font.Font(None, 18)

    def register_action(self, key, callback):
        self.actions[key] = callback

    def update(self, ball):
        for event in self.get_events():
            if event.type == QUIT:
                self.game.quit()
                sys.exit()

        keys = self.game.key.get_pressed()
        for reg in self.actions:
            #eval有个类似的函数exec， 但是返回值always None
            if eval(reg):
                self.actions[reg]()

        if not self.paused:
            ball.move()

    def get_events(self):
        return self.game.event.get()

    def draw(self, image):
        self.screen.blit(image.img, (image.x,image.y))
        
    def display_screen(self):
        self.game.display.update() #針對pygame的展示更新（flush）
    
    def pause(self):
        self.paused = not self.paused

    def load_level1(self):
        self.pick_level = True
        self.level = 1
    
    def load_level2(self):
        self.pick_level = True
        self.level = 2

    def load_level3(self):
        self.pick_level = True
        self.level = 3

    def load_level4(self):
        self.pick_level = True
        self.level = 4