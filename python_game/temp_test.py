"""
    用于测试相关库的API， 比如pygame
"""
import pygame
import os
from pygame.locals import *
import sys


def test_get_screen():
    base_path = os.path.abspath('.')
    paddle_path = base_path + "/paddle.png"

    pygame.init()
    screen = pygame.display.set_mode((800,600))
    pygame.display.set_caption("星空")
    font = pygame.font.Font(None, 18)

    space = pygame.image.load(paddle_path)

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
        keys = pygame.key.get_pressed()
        if keys[K_ESCAPE]:
            sys.exit()
        screen.blit(space, (0,0))
        pygame.display.update()



if __name__ == "__main__":
    test_get_screen()
