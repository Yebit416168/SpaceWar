import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理子弹"""
    def __init__(self,ai_game,ship):
        """在当前创建子弹类"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images\\spritesheets\\bullet.png')

        #加载子弹
        self.image_list = []
        self.index = 0
        self.rate = 5
        for i in range(2):
            rows = i % 2
            self.region = (10 * rows,0 ,10,28)
            self.sub_image = pygame.Surface.subsurface(self.image,self.region)
            self.image_list.append(self.sub_image)
        self.rect = self.sub_image.get_rect()
        self.rect.midtop = ship.rect.midtop
        self.y = float(self.rect.y)

    def update(self):
        """子弹的移动"""
        if self.rect.bottom <= 0:
            self.kill()
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """绘制子弹"""
        self.screen.blit(self.image_list[self.index],self.rect)
        if self.rate < 5:
            self.rate += 1
        else:
            self.rate = 0
            if self.index < 1:
                self.index += 1
            else:
                self.index = 0



