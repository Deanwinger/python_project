import pygame
from pygame.locals import *
import os
import sys

base_path = os.path.abspath('.')

class Paddle(object):
    def __init__(self, path, x=200, y=400, speed=.5):
        self.img = self.image_from_path(path)
        self.x = x
        self.y = y
        self.speed = speed

    def image_from_path(self, path):
        img = pygame.image.load(path).convert_alpha()
        return img

    def move_left(self):
        self.x -= self.speed
    
    def move_right(self):
        self.x += self.speed

class Ball(object):
    def __init__(self, path, x=100, y=300, speed=1):
        self.img = self.image_from_path(path)
        self.x = x
        self.y = y
        self.speed = speed

    def image_from_path(self, path):
        img = pygame.image.load(path).convert_alpha()
        return img

    def move(self):
        pass

class GuaGame(object):
    def __init__(self):
        self.game = pygame
        self.screen = pygame.display.set_mode((800,600))

    def set_background(self):
        self.screen.fill([255,255,255])
    
    def init_pygame(self):
        self.game.init()
        self.game.display.set_caption("撞砖块")
        self.game.font.Font(None, 18)
        # self.set_background() 

    def update(self, paddle):
        for event in self.get_events():
            if event.type == QUIT:
                self.game.quit()
                sys.exit()

        keys = self.game.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
        elif keys[K_a]:
            paddle.move_left()
        elif keys[K_d]:
            paddle.move_right()
    
    def get_events(self):
        return self.game.event.get()

    def draw(self, image):
        self.screen.blit(image.img, (image.x,image.y))
        
    def display_screen(self):
        self.game.display.update() #針對pygame的展示更新（flush）

def main():
    gua = GuaGame()
    gua.init_pygame()

    paddle_path = base_path + "/paddle.png"
    paddle = Paddle(paddle_path)

    ball_path = base_path + "/ball.png"
    ball = Ball(ball_path)

    # clock=pygame.time.Clock()
    while True:
        gua.set_background()
        gua.update(paddle)
        gua.draw(paddle)
        gua.draw(ball)
        gua.display_screen()


if __name__ == "__main__":
    main()