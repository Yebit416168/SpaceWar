import pygame
import random
from gamesprite import GameSprite

SCREEN_RECT = pygame.Rect(0, 0, 512, 544)



class Alien1(GameSprite):
    """外星人类"""
    def __init__(self,ai_game):
        """初始化外星人位置"""
        super().__init__('images\\spritesheets\\alien1.png')
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        
        #指定敌机的初始随机速度 2-3
        self.speed = random.randint(self.settings.min_alien_speed, + self.settings.max_alien_speed)
        self.health = 5
        self.image_list = []
        self.index = 0
        self.rate = 2
        for i in range(2):
            rows = i % 2
            self.region = (64 * rows,0 ,64,32)
            self.sub_image = pygame.Surface.subsurface(self.image,self.region)
            self.image_list.append(self.sub_image)
        self.rect = self.sub_image.get_rect()

        #指定敌机的初始随机位置
        self.rect.bottom = 0
        self.rect.x = random.randint(0, (SCREEN_RECT.width-self.rect.width))
        self.explode_index = 0

    def update(self):
        """外星人移动"""
        super().update()

        #判断是否飞出屏幕，如果是，需要从精灵中删除敌机
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()

    def draw_alien(self):
        """绘制外星人"""
        self.screen.blit(self.image_list[self.index],self.rect)
        if self.rate < 5:
            self.rate += 1
        else:
            self.rate = 0
            if self.index < 1:
                self.index += 1
            else:
                self.index = 0

              
