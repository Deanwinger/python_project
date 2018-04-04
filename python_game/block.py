import pygame
from pygame.locals import *
from utils import recIntersects

class Block(pygame.sprite.Sprite):
    def __init__(self, x=100, y=100, lives=1):
        pygame.sprite.Sprite.__init__(self)
        # self.img = self.image_from_path(path)
        image_surface = pygame.surface.Surface([50,20])
        image_surface.fill([0,0,0])
        self.img = image_surface.convert()
        self.rect = self.img.get_rect()
        self.x = self.rect.left =  x
        self.y = self.rect.top = y
        self.width,self.height = self.img.get_size()
        self.alive = True
        self.lives = lives

    def kill(self):
        self.lives -= 1
        if self.lives < 1:
            self.alive = False

    def collided(self, ball):
        return self.alive and \
            (recIntersects(self, ball) or recIntersects(ball, self))