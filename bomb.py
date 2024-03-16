import pygame
from gamesprite import GameSprite

class Bomb(GameSprite):
    def __init__(self,ai_game):
        #爆炸效果用的如下属性
        self.screen = ai_game.screen
        self.image_index = 0
        self.image = [pygame.image.load("images\\spritesheets\\bomb" + str(ix) + ".png") for ix in range(5)]
        
        #用来记录while True的次数,当次数达到一定值时才显示一张爆炸的图,然后清空,,当这个次数再次达到时,再显示下一个爆炸效果的图片
        self.inerval = 20
        self.inerval_index = 0
        self.position = [0,0]

        self.visible = False

    def draw_bomb(self):
        """绘制爆炸"""
        if not self.visible:
            return

        self.inerval_index += 1
        #每20次循环换一张图片
        if self.inerval_index < self.inerval:
            return
        self.inerval = 0
        self.image_index += 1
        if self.image_index > 4:
            self.image_index = 0
            self.visible = False
        
        self.screen.blit(self.image[self.image_index], (self.position[0],self.position[1]))
