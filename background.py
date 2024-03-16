import pygame
from settings import Settings

#屏幕大小的常量
SCREEN_RECT = pygame.Rect(0,0,512,544)

class BackgroundSprite(pygame.sprite.Sprite):
    """背景精灵"""
    def __init__(self, image_name,speed = 1):
        super().__init__()
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed

    def update(self):
        """背景移动"""
        self.rect.y += self.speed

class Background(BackgroundSprite):
    """游戏背景精灵"""
    def update(self):
        #调用父类的方法实现：垂直移动
        super().update()

        #判断是否移出屏幕，若移出屏幕，应该将图像设置到图像上方
        if self.rect.y >= SCREEN_RECT.height:
            self.rect.y = -self.rect.height