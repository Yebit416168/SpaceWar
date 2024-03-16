import pygame
import random
from pygame.sprite import Sprite

SCREEN_RECT = pygame.Rect(0, 0, 512, 544)

class BloodPacks(Sprite):
    """血包类"""
    def __init__(self,ai_game):
        """创建血包"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images\\spritesheets\\health.png')

        self.speed = 3
        self.rect = self.image.get_rect()

        #指定血包的初始随机位置
        self.rect.bottom = 0
        self.rect.x = random.randint(0, (SCREEN_RECT.width-self.rect.width))
        self.y = float(self.rect.y)

    def update(self):
        if self.rect.y > 544:
            self.kill()
        self.y += self.speed
        self.rect.y = self.y

    def draw_bloodpacks(self):
        self.screen.blit(self.image,self.rect)

class MinecraftLaunch(Sprite):
    """我的世界启动类"""
    def __init__(self,ai_game):
        """创建启动"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images\\spritesheets\\Minecraft.png')
        self.minecraft = False

        self.speed = 3
        self.rect = self.image.get_rect()

        self.rect.bottom = 0
        self.rect.x = random.randint(0, (SCREEN_RECT.width-self.rect.width))
        self.y = float(self.rect.y)

    def update(self):
        if self.rect.y > 544:
            self.kill()
        self.y += self.speed
        self.rect.y = self.y

    def draw_minecraftlaunch(self):
        self.screen.blit(self.image,self.rect)

class YuanLaunch(Sprite):
    """原神启动类"""
    def __init__(self,ai_game):
        """创建启动"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.image = pygame.image.load('images\\spritesheets\\yuan.png')
        self.minecraft = False

        self.speed = 3
        self.rect = self.image.get_rect()


        self.rect.bottom = 0
        self.rect.x = random.randint(0, (SCREEN_RECT.width-self.rect.width))
        self.y = float(self.rect.y)

    def update(self):
        if self.rect.y > 544:
            self.kill()
        self.y += self.speed
        self.rect.y = self.y

    def draw_yuan(self):
        self.screen.blit(self.image,self.rect)
