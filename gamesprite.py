import pygame

class GameSprite(pygame.sprite.Sprite):
    """游戏精灵"""

    def __init__(self, image_name, speed=1, speed2=1):

        # 调用父类的初始化方法
        super().__init__()
        # 定义对象的属性
        self.image = pygame.image.load(image_name)
        self.rect = self.image.get_rect()
        self.speed = speed
        self.speed2 = speed2
    def update(self):
        # 在屏幕的垂直方向上移动
        self.rect.y += self.speed