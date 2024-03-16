import pygame
from settings import Settings
from gamesprite import GameSprite

SCREEN_RECT = pygame.Rect(0,0,512,544)

class Ship(GameSprite):
    """飞船的类"""
    def __init__(self,ai_game):
        """初始飞船的位置"""
        super().__init__('images\\spritesheets\\ship.png')
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.health_screen = ai_game.screen
        self.health_screen_rect = self.health_screen.get_rect()
        self.settings = ai_game.settings
        self.ship_bomb_index = 0
        self.health = 100
        self.health_death = False
        self.ship_index = 0
        self.font = pygame.font.Font("font\\Minecraft.ttf", 16)
        self.health_image = self.font
        self.screen = ai_game.screen = pygame.display.set_mode((SCREEN_RECT.width,SCREEN_RECT.height))
        
        #加载飞船
        self.image_list = []
        self.index = 0
        self.rate = 2
        for i in range(10):
            columns= i // 5
            rows = i % 5
            self.region = (32 * rows,48 * columns,32,48)
            self.sub_image = pygame.Surface.subsurface(self.image,self.region)
            self.image_list.append(self.sub_image)
        self.rect = self.sub_image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        #float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #移动方向属性
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.prep_ships()

    def prep_ships(self):
        """显示血量"""
        health_str = f"玩家1血量:{self.health}"
        self.health_image = self.font.render(health_str,True,(255,255,255), None)

        #上角显示分数
        self.health_rect = self.health_image.get_rect()
        self.health_rect.left =self.screen_rect.left
        self.health_rect.top = 0
    
    def update(self):
        """调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        #更新
        self.rect.x = self.x
        self.rect.y = self.y
        if self.health == 0:
            self.kill()

    def blitme(self):
        """绘制飞船"""
        self.screen.blit(self.image_list[self.index],self.rect)
        if self.rate < 2:
            self.rate += 1
        else:
            self.rate = 0
            if self.index < 9:
                self.index += 1
            else:
                self.index = 0
    
    def draw_health(self):
        self.screen.blit(self.health_image,self.health_rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom

class Ship1(GameSprite):
    """飞船的类"""
    def __init__(self,ai_game):
        """初始飞船的位置"""
        super().__init__('images\\spritesheets\\ship1.png')
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.health_screen = ai_game.screen
        self.health_screen_rect = self.health_screen.get_rect()
        self.settings = ai_game.settings
        self.ship_bomb_index = 0
        self.health = 100
        self.health_death = False
        self.ship_index = 0
        self.font = pygame.font.Font("font\\Minecraft.ttf", 16)
        self.health_image = self.font
        self.screen = ai_game.screen = pygame.display.set_mode((SCREEN_RECT.width,SCREEN_RECT.height))
        
        #加载飞船
        self.image_list = []
        self.index = 0
        self.rate = 2
        for i in range(10):
            columns= i // 5
            rows = i % 5
            self.region = (32 * rows,48 * columns,32,48)
            self.sub_image = pygame.Surface.subsurface(self.image,self.region)
            self.image_list.append(self.sub_image)
        self.rect = self.sub_image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom

        #float
        self.x = float(self.rect.x)
        self.y = float(self.rect.y)
        #移动方向属性
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.prep_ships()

    def prep_ships(self):
        """显示血量"""
        health_str = f"玩家2血量:{self.health}"
        self.health_image = self.font.render(health_str,True,(255,255,255), None)

        #上角显示分数
        self.health_rect = self.health_image.get_rect()
        self.health_rect.left =self.screen_rect.left
        self.health_rect.top = 20
    
    def update(self):
        """调整飞船的位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        if self.moving_up and self.rect.top > 0:
            self.y -= self.settings.ship_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.y += self.settings.ship_speed

        #更新
        self.rect.x = self.x
        self.rect.y = self.y
        if self.health == 0:
            self.kill()

    def blitme(self):
        """绘制飞船"""
        self.screen.blit(self.image_list[self.index],self.rect)
        if self.rate < 2:
            self.rate += 1
        else:
            self.rate = 0
            if self.index < 9:
                self.index += 1
            else:
                self.index = 0
    
    def draw_health(self):
        self.screen.blit(self.health_image,self.health_rect)

    def center_ship(self):
        self.rect.midbottom = self.screen_rect.midbottom
