import pygame
from pygame.locals import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, path, x=100, y=300, speedX=0.4, speedY=0.4):
        pygame.sprite.Sprite.__init__(self)
        self.img = self.image_from_path(path)
        # image_surface = pygame.surface.Surface([10,10])
        # image_surface.fill([0,0,0])
        # self.img = image_surface.convert()
        self.rect = self.img.get_rect()
        self.x = self.rect.left =  x
        self.y = self.rect.top = y
        self.speedX = speedX
        self.speedY = speedY
        self.width,self.height = self.img.get_size()
        self.fired = False

    def image_from_path(self, path):
        img = pygame.image.load(path)
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

    def bounce_back(self):
        self.speedY = -self.speedY