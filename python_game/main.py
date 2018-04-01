import pygame
from pygame.locals import *
import os
import sys

base_path = os.path.abspath('.')

class Paddle(pygame.sprite.Sprite):
    def __init__(self, path, x=200, y=400, speed=.5):
        pygame.sprite.Sprite.__init__(self)
        self.img = self.image_from_path(path)
        self.x = x
        self.y = y
        self.speed = speed
        self.rect = self.img.get_rect()

    def image_from_path(self, path):
        img = pygame.image.load(path).convert_alpha()
        return img

    def move_left(self):
        self.x -= self.speed
    
    def move_right(self):
        self.x += self.speed

    # def collide(self, ball):


class Ball(pygame.sprite.Sprite):
    def __init__(self, path, x=100, y=300, speedX=0.4, speedY=0.4):
        pygame.sprite.Sprite.__init__(self)
        self.img = self.image_from_path(path)
        self.x = x
        self.y = y
        self.speedX = speedX
        self.speedY = speedY
        self.fired = False
        self.rect = self.img.get_rect()
        

    def image_from_path(self, path):
        img = pygame.image.load(path).convert_alpha()
        return img

    def move(self):
        if self.fired:
            if self.x < 0 or self.x > 800:
                self.speedX = -self.speedX
            if self.y < 0 or self.y > 600:
                self.speedY = -self.speedY
            
            self.x += self.speedX
            self.y += self.speedY
            
    def fire(self):
        self.fired = True


class GuaGame(object):
    def __init__(self):
        self.game = pygame
        self.screen = pygame.display.set_mode((800,600))
        self.actions = {}

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
        
        ball.move()

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
    # ballGroup = gua.game.sprite.Group(ball)

    gua.register_action('keys[K_ESCAPE]', sys.exit)
    gua.register_action('keys[K_a]', paddle.move_left)
    gua.register_action('keys[K_d]', paddle.move_right)
    gua.register_action('keys[K_f]', ball.fire)

    # clock=pygame.time.Clock()
    while True:
        gua.set_background()
        gua.update(ball)
        # if gua.game.sprite.spritecollide(paddle, ballGroup,False):
        #     ball.speedY = - ball.speedY
        gua.draw(paddle)
        gua.draw(ball)
        gua.display_screen()


if __name__ == "__main__":
    main()