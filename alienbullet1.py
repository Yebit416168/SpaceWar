import pygame
from pygame.sprite import Sprite

class AlienBulletLeft(Sprite):
    """管理子弹"""
    def __init__(self,ai_game):
        """在当前创建子弹类"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images\\spritesheets\\alienbullet.png')

        #加载子弹
        self.speed = self.settings.bullet_speed + self.settings.diffculty
        self.image_list = []
        self.index = 0
        self.rate = 5
        for i in range(2):
            rows = i % 2
            self.region = (10 * rows,0 ,10,10)
            self.sub_image = pygame.Surface.subsurface(self.image,self.region)
            self.image_list.append(self.sub_image)
        self.rect = self.sub_image.get_rect()
        self.rect.left = ai_game.aliens1.rect.left
        
        self.y = float(self.rect.y)

    def update(self):
        """子弹的移动"""
        if self.rect.y > 544:
            self.kill()
        self.y += self.speed
        self.rect.y = self.y
        

    def draw_bullet(self):
        """绘制子弹"""
        self.screen.blit(self.image_list[self.index],(self.rect.left + 15,self.rect.y))
        if self.rate < 5:
            self.rate += 1
        else:
            self.rate = 0
            if self.index < 1:
                self.index += 1
            else:
                self.index = 0

class AlienBulletRight(Sprite):
    """管理子弹"""
    def __init__(self,ai_game):
        """在当前创建子弹类"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images\\spritesheets\\alienbullet.png')

        #加载子弹
        self.speed = self.settings.bullet_speed + self.settings.diffculty
        self.image_list = []
        self.index = 0
        self.rate = 5
        for i in range(2):
            rows = i % 2
            self.region = (10 * rows,0 ,10,10)
            self.sub_image = pygame.Surface.subsurface(self.image,self.region)
            self.image_list.append(self.sub_image)
        self.rect = self.sub_image.get_rect()
        self.rect.right = ai_game.aliens1.rect.right
        
        self.y = float(self.rect.y)

    def update(self):
        """子弹的移动"""
        if self.rect.y> 544:
            self.kill()
        self.y += self.speed
        self.rect.y = self.y

    def draw_bullet(self):
        """绘制子弹"""
        self.screen.blit(self.image_list[self.index],(self.rect.right - 15,self.rect.y))
        if self.rate < 5:
            self.rate += 1
        else:
            self.rate = 0
            if self.index < 1:
                self.index += 1
            else:
                self.index = 0