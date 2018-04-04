import pygame
from pygame.locals import *
import os
import sys
from guagame import GuaGame
from ball import Ball
from paddle import Paddle
from block import Block
from level import levels

base_path = os.path.abspath('.')

def loadlevel(n):
    blocks = []
    n -= 1
    level = levels[n]
    for x, y, z in level:
        b = Block(x, y, z)
        blocks.append(b)
    return blocks


def main():
    gua = GuaGame()
    gua.init_pygame()

    paddle_path = base_path + "/paddle.png"
    paddle = Paddle(paddle_path)

    ball_path = base_path + "/ball.png"
    ball = Ball(ball_path)

    gua.register_action('keys[K_ESCAPE]', sys.exit)
    gua.register_action('keys[K_a]', paddle.move_left)
    gua.register_action('keys[K_d]', paddle.move_right)
    gua.register_action('keys[K_f]', ball.fire)
    gua.register_action('keys[K_p]', gua.pause)
    gua.register_action('keys[K_1]', gua.load_level1)
    gua.register_action('keys[K_2]', gua.load_level2)
    gua.register_action('keys[K_3]', gua.load_level3)
    gua.register_action('keys[K_4]', gua.load_level4)

    blocks = loadlevel(gua.level)
    clock=pygame.time.Clock()
    fps = 500

    textpos = [750,10]
    points = 0
    while True:
        if gua.pick_level:
            blocks = loadlevel(gua.level)
            gua.pick_level = False

        clock.tick(fps)
        gua.set_background()
        if paddle.collided(ball):
            ball.bounce_back()

        # 应该与blocks相撞
        for block in blocks:
            if block.collided(ball):
                block.kill()
                ball.bounce_back()
        
        gua.update(ball)
        gua.draw(paddle)
        gua.draw(ball)
        for block in blocks:
            if block.alive:
                gua.draw(block)
        
        font = pygame.font.Font(None,50)
        score_text = font.render(str(points),1,(0,200,0))
        gua.screen.blit(score_text,textpos)

        gua.display_screen()




if __name__ == "__main__":
    main()