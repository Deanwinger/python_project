import pygame
from pygame.locals import *
from utils import recIntersects


class Paddle(pygame.sprite.Sprite):
    def __init__(self, path, x=200, y=400, speed=.5):
        pygame.sprite.Sprite.__init__(self)
        self.img = self.image_from_path(path)
        # image_surface = pygame.surface.Surface([100,20])
        # image_surface.fill([0,0,0])
        # self.img = image_surface.convert()
        self.rect = self.img.get_rect()
        self.x = self.rect.left =  x
        self.y = self.rect.top = y
        self.speed = speed
        self.rect = self.img.get_rect()
        self.width,self.height = self.img.get_size()

    def image_from_path(self, path):
        img = pygame.image.load(path)
        return img

    def move(self, x):
        self.x = x
        if self.x < 0:
            self.x = 0
        if self.x > 800 - self.width:
            self.x = 800 - self.width

    def move_left(self):
        self.move(self.x - self.speed)
    
    def move_right(self):
        self.move(self.x + self.speed)

    def collided(self, ball):
        return recIntersects(self, ball) or recIntersects(ball, self)


