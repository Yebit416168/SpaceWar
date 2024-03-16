import sys
import pygame
from settings import Settings
from player import Ship,Ship1
from button import Button,ButtonPlayer,ButtonPlayer1
from bullet import Bullet
from alienbullet import AlienBullet
from alienbullet1 import AlienBulletLeft,AlienBulletRight
from alienbullet2 import AlienBulletLeft2,AlienBulletMidtop2,AlienBulletRight2
from skill import BloodPacks,MinecraftLaunch,YuanLaunch
from alien import Alien
from alien1 import Alien1
from alien2 import Alien2
from scoreboard import Scoreboard
from bomb import *
from background import *
from contextlib import suppress

with suppress(ModuleNotFoundError):
    import pyi_splash
    pyi_splash.close()

SCREEN_RECT = pygame.Rect(0,0,512,544)
CRATE_ALIEN_EVENT = pygame.USEREVENT

class AlienInvasion():
    def __init__(self):
        """初始游戏创建游戏资源"""
        pygame.init()
        pygame.mixer.init()
        self.bgm = pygame.mixer.music
        self.bgm.load("music\\C418.ogg")
        self.bgm.play()


        self.clock = pygame.time.Clock()
        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (SCREEN_RECT.width,SCREEN_RECT.height))
        
        self.score_game = Scoreboard(self)
        self.player = False

        self.musicx = 1
        self.musicy = 1
        self.m =pygame.mixer.Sound("music\\duolian.ogg")
        
        #创建外星人的定时器
        pygame.time.set_timer(CRATE_ALIEN_EVENT, 1500)
        
        #窗体名字
        pygame.display.set_caption("太空大战")

        self._create_sprites()

        #让游戏处于非活动状态
        self.play_button = Button(self,"重新开始")
        self.player_button = ButtonPlayer(self,"单人")
        self.player_button1 = ButtonPlayer1(self,"双人")
        self.game_active = False

    def _create_sprites(self):

        #创建背景精灵和精灵组
        bg1 = Background('images\\backgrounds\\desert-backgorund.png')
        bg2 = Background('images\\backgrounds\\desert-backgorund1.png')
        bg2.rect.y =- bg2.rect.height
        self.back_group = pygame.sprite.Group(bg1, bg2)

        # 创建敌机的精灵组
        self.aliens = Alien(self)
        self.alien_group = pygame.sprite.Group()

        self.aliens1 = Alien1(self)
        self.alien_group1 = pygame.sprite.Group()

        self.aliens2 = Alien2(self)
        self.alien_group2 = pygame.sprite.Group()
        
        # 创建飞船的精灵组
        self.ship1 = Ship1(self)
        self.ship_group1 = pygame.sprite.Group(self.ship1)
        
        self.ship = Ship(self)
        self.ship_group = pygame.sprite.Group(self.ship)

        # 创建爆炸精灵组
        self.bombs = [Bomb(self) for _ in range(5)]
        #创建血包精灵组
        
        self.bullets = pygame.sprite.Group()
        self.bulletmidtops = pygame.sprite.Group()
        self.bulletlefts = pygame.sprite.Group()
        self.bulletrights = pygame.sprite.Group()
        self.alienbullets = pygame.sprite.Group()
        self.alienbulletsleft1 = pygame.sprite.Group()
        self.alienbulletsright1 = pygame.sprite.Group()
        self.alienbulletsmidtop2 = pygame.sprite.Group()
        self.alienbulletsleft2 = pygame.sprite.Group()
        self.alienbulletsright2 = pygame.sprite.Group()
        self.blookpacks = pygame.sprite.Group()
        self.minecraftLaunchs = pygame.sprite.Group()
        self.minecraftLaunch = MinecraftLaunch(self)
        self.yuanlaunch = YuanLaunch(self)
        self.yuanlaunchs = pygame.sprite.Group()
    
    def _check_collide(self):
        """技能碰撞检测"""
        for yuan in self.yuanlaunchs:
            #启动碰撞
            ship_collide_yuanlaunch_launch = pygame.sprite.groupcollide(self.ship_group,self.yuanlaunchs,False,True)
            collide_yuanlaunch_launch = pygame.sprite.groupcollide(self.ship_group1,self.yuanlaunchs,False,True)
            if ship_collide_yuanlaunch_launch or collide_yuanlaunch_launch:
                self.score_game.score += 1000
                yuanmusic = pygame.mixer.Sound("music\\yuan.ogg")
                yuanmusic.play()

        for minecraft in self.minecraftLaunchs:
            #我的世界启动碰撞
            ship_collide_minecraft_launch = pygame.sprite.groupcollide(self.ship_group,self.minecraftLaunchs,False,True)
            collide_minecraft_launch = pygame.sprite.groupcollide(self.ship_group1,self.minecraftLaunchs,False,True)
            if ship_collide_minecraft_launch or collide_minecraft_launch:
                UPEXP = pygame.mixer.Sound("music\\UPEXP.ogg")
                UPEXP.play()
                #清空精灵
                self.bullets.empty()
                self.alienbullets.empty()
                self.alienbulletsleft1.empty()
                self.alienbulletsright1.empty()
                self.alienbulletsleft2.empty()
                self.alienbulletsmidtop2.empty()
                self.alienbulletsright2.empty()
                self.alien_group.empty()
                self.alien_group1.empty()
                self.alien_group2.empty()
                

        for blookpack in self.blookpacks:
            #血包碰撞
            ship_collide_blookpack = pygame.sprite.groupcollide(self.ship_group,self.blookpacks,False,True)
            collide_blookpack = pygame.sprite.groupcollide(self.ship_group1,self.blookpacks,False,True)
            if ship_collide_blookpack or collide_blookpack:
                self.ship.health = 100
                self.ship1.health = 100
                blookpack_music = pygame.mixer.Sound("music\\health.ogg")
                blookpack_music.play()

                blookpack_music.play()

    def alien_check_collide(self):
        """外星人碰撞"""
        for bullet in self.bullets:
            collisions = pygame.sprite.groupcollide(self.bullets,self.alien_group,True,True)
            collisions1 = pygame.sprite.groupcollide(self.bullets,self.alien_group1,True,True)
            collisions2 = pygame.sprite.groupcollide(self.bullets,self.alien_group2,True,True)
            if collisions:
                bomb_muic = pygame.mixer.Sound("music\\bomb.ogg")
                bomb_muic.set_volume(0.2)
                bomb_muic.play()
                for alien_group in collisions.values():
                    self.score_game.score += 10 * len(alien_group)
                current_pos = pygame.Vector2(bullet.rect.x, bullet.rect.y)
                if bullet.rect.collidepoint(current_pos):
                    for bomb in self.bombs:
                        if not bomb.visible:
                            bomb.position[0] = (bullet.rect.x - 20)
                            bomb.position[1] = (bullet.rect.y - 40)
                            bomb.visible = True
        
            if collisions1:
                bomb_muic = pygame.mixer.Sound("music\\bomb.ogg")
                bomb_muic.set_volume(0.2)
                bomb_muic.play()
                for alien_group1 in collisions1.values():
                    self.score_game.score+= 30 * len(alien_group1)
                current_pos1 = pygame.Vector2(bullet.rect.x, bullet.rect.y)
                if bullet.rect.collidepoint(current_pos1):
                    for bomb in self.bombs:
                        if not bomb.visible:
                            bomb.position[0] = (bullet.rect.x - 20)
                            bomb.position[1] = (bullet.rect.y - 40)
                            bomb.visible = True
            if collisions2:
                bomb_muic = pygame.mixer.Sound("music\\bomb.ogg")
                bomb_muic.set_volume(0.2)
                bomb_muic.play()
                for alien_group2 in collisions2.values():
                    self.score_game.score += 50 * len(alien_group2)
                current_pos2 = pygame.Vector2(bullet.rect.x, bullet.rect.y)
                if bullet.rect.collidepoint(current_pos2):
                    for bomb in self.bombs:
                        if not bomb.visible:
                            bomb.position[0] = (bullet.rect.x - 20)
                            bomb.position[1] = (bullet.rect.y - 40)
                            bomb.visible = True


            
            self._check_high_score()
            self.score_game.prep_high_score()

    def ship_check_collide(self):
        """玩家碰撞"""
        for ship in self.ship_group:
            ship_collide = pygame.sprite.groupcollide(self.ship_group,self.alien_group,self.ship.health_death,True)
            ship_collide1 = pygame.sprite.groupcollide(self.ship_group,self.alien_group1,self.ship.health_death,True)
            ship_collide2 = pygame.sprite.groupcollide(self.ship_group,self.alien_group2,self.ship.health_death,True)
            bullet_ship_collide = pygame.sprite.groupcollide(self.ship_group,self.alienbullets,self.ship.health_death,True)
            bullet_ship_collide_left1 = pygame.sprite.groupcollide(self.ship_group,self.alienbulletsleft1,self.ship.health_death,True)
            bullet_ship_collide_right1 = pygame.sprite.groupcollide(self.ship_group,self.alienbulletsright1,self.ship.health_death,True)
            bullet_ship_collide_midtop2 = pygame.sprite.groupcollide(self.ship_group,self.alienbulletsmidtop2,self.ship.health_death,True)
            bullet_ship_collide_left2 = pygame.sprite.groupcollide(self.ship_group,self.alienbulletsleft2,self.ship.health_death,True)
            bullet_ship_collide_right2 = pygame.sprite.groupcollide(self.ship_group,self.alienbulletsright2,self.ship.health_death,True)
            if ship_collide or ship_collide1 or ship_collide2:
                ship.health -= 10
                bomb_muic = pygame.mixer.Sound("music\\bomb.ogg")
                bomb_muic.set_volume(0.2)
                bomb_muic.play()
                if ship.health <= 0:
                    ship.health = 0
                    ship.health_death = True
                if ship.health_death and self.ship1.health_death:
                    self.game_active = False
                elif ship.health_death and not self.player:
                    self.game_active = False
                    pygame.mouse.set_visible(True)
                for bomb in self.bombs:
                    if not bomb.visible:
                        bomb.position[0] = (self.ship.rect.x)
                        bomb.position[1] = (self.ship.rect.y - 40)
                        
                        bomb.visible = True
            if bullet_ship_collide or bullet_ship_collide_left1 or bullet_ship_collide_right1 or bullet_ship_collide_midtop2 or bullet_ship_collide_left2 or bullet_ship_collide_right2:
                ship.health -= 10
                bomb_muic = pygame.mixer.Sound("music\\bomb.ogg")
                bomb_muic.set_volume(0.2)
                bomb_muic.play()
                if ship.health <= 0:
                    ship.health = 0
                    ship.health_death = True
                    if ship.health_death and  self.ship1.health_death:
                        self.game_active = False
                    elif ship.health_death and not self.player:
                        self.game_active = False
                    pygame.mouse.set_visible(True)
                    for bomb in self.bombs:
                        if not bomb.visible:
                            bomb.position[0] = (self.ship.rect.x)
                            bomb.position[1] = (self.ship.rect.y - 40)
                            bomb.visible = True
        
        for ship1 in self.ship_group1:
            if self.player:
                collide = pygame.sprite.groupcollide(self.ship_group1,self.alien_group,self.ship1.health_death,True)
                collide1 = pygame.sprite.groupcollide(self.ship_group1,self.alien_group1,self.ship1.health_death,True)
                collide2 = pygame.sprite.groupcollide(self.ship_group1,self.alien_group2,self.ship1.health_death,True)
                ship_collide = pygame.sprite.groupcollide(self.ship_group1,self.alienbullets,self.ship1.health_death,True)
                ship_collide_left1 = pygame.sprite.groupcollide(self.ship_group1,self.alienbulletsleft1,self.ship1.health_death,True)
                ship_collide_right1 = pygame.sprite.groupcollide(self.ship_group1,self.alienbulletsright1,self.ship1.health_death,True)
                ship_collide_midtop2 = pygame.sprite.groupcollide(self.ship_group1,self.alienbulletsmidtop2,self.ship1.health_death,True)
                ship_collide_left2 = pygame.sprite.groupcollide(self.ship_group1,self.alienbulletsleft2,self.ship1.health_death,True)
                ship_collide_right2 = pygame.sprite.groupcollide(self.ship_group1,self.alienbulletsright2,self.ship1.health_death,True)
                if collide or collide1 or collide2:
                    ship1.health -= 10
                    bomb_muic = pygame.mixer.Sound("music\\bomb.ogg")
                    bomb_muic.set_volume(0.2)
                    bomb_muic.play()
                    if ship1.health <= 0:
                        ship1.health = 0
                        ship1.health_death = True
                        if self.ship.health_death and ship1.health_death:
                            self.game_active = False
                        pygame.mouse.set_visible(True)
                    for bomb in self.bombs:
                        if not bomb.visible:
                            bomb.position[0] = (self.ship1.rect.x)
                            bomb.position[1] = (self.ship1.rect.y - 40)
                            
                            bomb.visible = True
                if ship_collide or ship_collide_left1 or ship_collide_right1 or ship_collide_midtop2 or ship_collide_left2 or ship_collide_right2:
                    ship1.health -= 10
                    bomb_muic = pygame.mixer.Sound("music\\bomb.ogg")
                    bomb_muic.set_volume(0.2)
                    bomb_muic.play()
                    if ship1.health <= 0:
                        ship1.health = 0
                        ship1.health_death = True
                    if self.ship.health_death and ship1.health_death:
                        self.game_active = False
                        pygame.mouse.set_visible(True)
                        for bomb in self.bombs:
                            if not bomb.visible:
                                bomb.position[0] = (self.ship1.rect.x)
                                bomb.position[1] = (self.ship1.rect.y - 40)
                                bomb.visible = True
                
            
    def _check_events(self):
        """响应按键鼠标"""
        for event in pygame.event.get():
            #玩家1
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    self.ship.moving_right = True
                elif event.key == pygame.K_a:
                    self.ship.moving_left = True
                elif event.key == pygame.K_w:
                    self.ship.moving_up = True
                elif event.key == pygame.K_s:
                    self.ship.moving_down = True
                elif event.key == pygame.K_j:
                    if self.game_active and not self.ship.health_death:
                        self.player_fire_bullet(self.ship)
                elif event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d:
                    self.ship.moving_right = False
                elif event.key == pygame.K_a:
                    self.ship.moving_left = False
                elif event.key == pygame.K_w:
                    self.ship.moving_up = False
                elif event.key == pygame.K_s:
                    self.ship.moving_down = False
            #玩家2
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship1.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship1.moving_left = True
                elif event.key == pygame.K_UP:
                    self.ship1.moving_up = True
                elif event.key == pygame.K_DOWN:
                    self.ship1.moving_down = True
                elif event.key == pygame.K_KP0:
                    if self.game_active and not self.ship1.health_death and self.player:
                        self.player_fire_bullet1(self.ship1)
                
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship1.moving_right = False
                elif event.key == pygame.K_LEFT:
                    self.ship1.moving_left = False
                elif event.key == pygame.K_UP:
                    self.ship1.moving_up = False
                elif event.key == pygame.K_DOWN:
                    self.ship1.moving_down = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == CRATE_ALIEN_EVENT:
                for i in range(self.settings.diffculty + 1):
                    if self.game_active:
                        self.aliens = Alien(self)
                        self.alien_group.add(self.aliens)
                        alienbullet = AlienBullet(self)
                        self.alienbullets.add(alienbullet)

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == CRATE_ALIEN_EVENT:
                for i in range(self.settings.diffculty + 1):
                    if self.game_active:
                        self.aliens1 = Alien1(self)
                        self.alien_group1.add(self.aliens1)
                        alienbulletleft1 = AlienBulletLeft(self)
                        self.alienbulletsleft1.add(alienbulletleft1)
                        alienbulletright1 = AlienBulletRight(self)
                        self.alienbulletsright1.add(alienbulletright1)


            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == CRATE_ALIEN_EVENT:
                for i in range(self.settings.diffculty + 1):
                    if self.game_active:
                        self.aliens2 = Alien2(self)
                        self.alien_group2.add(self.aliens2)
                        alienbulletmidtop2 = AlienBulletMidtop2(self)
                        self.alienbulletsmidtop2.add(alienbulletmidtop2)
                        alienbulletleft2 = AlienBulletLeft2(self)
                        self.alienbulletsleft2.add(alienbulletleft2)
                        alienbulletright2 = AlienBulletRight2(self)
                        self.alienbulletsright2.add(alienbulletright2)

    def _check_play_button(self,mouse_pos):
        """在点击开始按钮时"""
        button_clicked = self.play_button.rect.collidepoint(mouse_pos)
        button_clicked1 = self.player_button.rect.collidepoint(mouse_pos)
        button_clicked2 = self.player_button1.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.minecraftLaunch.minecraft = False
            self.score_game.score = 0
            self.settings.diffculty = 0
            self.ship.health = 100
            self.musicy = 1
            self.musicx = 1
            self.m.stop()
            self.bgm.play()
            self.score_game.exp_level = 0
            self.score_game.sscore_level = 2000
            self.score_game.launch = 0
            self.score_game.minecraft_launch = 4000
            self.score_game.yuanlaunch = 0
            self.score_game.yuanlaunch_launch = 1000
            if self.player:
                self.player = True
            elif not self.player:
                self.player = False
            self.ship.health_death = False
            self.game_active = True
            #清空精灵
            self.bullets.empty()
            self.alienbullets.empty()
            self.alienbulletsleft1.empty()
            self.alienbulletsright1.empty()
            self.alienbulletsleft2.empty()
            self.alienbulletsmidtop2.empty()
            self.alienbulletsright2.empty()
            self.alien_group.empty()
            self.alien_group1.empty()
            self.alien_group2.empty()

            #创建新精灵
            self._create_sprites()
            self.ship.center_ship()

            pygame.mouse.set_visible(False)
        if button_clicked2 and not self.game_active:
            self.minecraftLaunch.minecraft = False
            self.score_game.score = 0
            self.settings.diffculty = 0
            self.ship.health = 100
            self.musicy = 1
            self.musicx = 1
            self.m.stop()
            self.bgm.play()
            self.score_game.exp_level = 0
            self.score_game.sscore_level = 2000
            self.score_game.launch = 0
            self.score_game.minecraft_launch = 4000
            self.score_game.yuanlaunch = 0
            self.score_game.yuanlaunch_launch = 1000
            self.player = True
            self.ship1.health_death = False
            self.game_active = True
            #清空精灵
            self.bullets.empty()
            self.alienbullets.empty()
            self.alienbulletsleft1.empty()
            self.alienbulletsright1.empty()
            self.alienbulletsleft2.empty()
            self.alienbulletsmidtop2.empty()
            self.alienbulletsright2.empty()
            self.alien_group.empty()
            self.alien_group1.empty()
            self.alien_group2.empty()

            self._create_sprites()
            self.ship1.center_ship()
            
        if button_clicked1 and not self.game_active:
            self.minecraftLaunch.minecraft = False
            self.score_game.score = 0
            self.settings.diffculty = 0
            self.ship.health = 100
            self.musicy = 1
            self.musicx = 1
            self.m.stop()
            self.bgm.play()
            self.score_game.exp_level = 0
            self.score_game.sscore_level = 2000
            self.score_game.launch = 0
            self.score_game.minecraft_launch = 4000
            self.score_game.yuanlaunch = 0
            self.score_game.yuanlaunch_launch = 1000
            self.player = False
            self.ship.health_death = False
            self.game_active = True
            #清空精灵
            self.bullets.empty()
            self.alienbullets.empty()
            self.alienbulletsleft1.empty()
            self.alienbulletsright1.empty()
            self.alienbulletsleft2.empty()
            self.alienbulletsmidtop2.empty()
            self.alienbulletsright2.empty()
            self.alien_group.empty()
            self.alien_group1.empty()
            self.alien_group2.empty()

            #创建新精灵
            self._create_sprites()
            self.ship.center_ship()

            pygame.mouse.set_visible(False)

    def _check_high_score(self):
        if self.score_game.score > self.score_game.high_score:
            self.score_game.high_score = self.score_game.score
            self.score_game.prep_high_score()
                    
    def player_fire_bullet(self,player):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self,player)
            self.bullets.add(new_bullet)

        #删除子弹
        for bullet in self.bullets:
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
    def player_fire_bullet1(self,player1):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet1 = Bullet(self,player1)
            self.bullets.add(new_bullet1)

        #删除子弹
        for bullet in self.bullets:
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        
    def _update_screen(self):
        """更新屏幕"""
        #重绘屏幕
        self.score_game.prep_score()
        self.score_game.prep_diffculty()
        self.score_game.show_score()

        if self.settings.diffculty >= 15:
            self.settings.diffculty = 0


        if self.score_game.score >= self.score_game.exp_level + self.score_game.score_level:
            blook_packs = BloodPacks(self)
            self.blookpacks.add(blook_packs)
            self.score_game.exp_level += 500
        if self.score_game.score >= self.score_game.minecraft_launch + self.score_game.launch:
            minecraftlaunch = MinecraftLaunch(self)
            self.minecraftLaunchs.add(minecraftlaunch)
            self.score_game.launch += 2000
        if self.score_game.score >= self.score_game.yuanlaunch_launch + self.score_game.yuanlaunch:
            yuanlaunch = YuanLaunch(self)
            self.yuanlaunchs.add(yuanlaunch)
            self.score_game.yuanlaunch += 2000
        if self.score_game.score >= self.score_game.diffculty_score + self.score_game.diffculty_level:
            self.settings.diffculty += 1
            self.score_game.diffculty_level += 1000

        if self.score_game.score >= 10000 and self.musicx<= 1:
            play = pygame.mixer.Sound("music\\score.ogg")
            play.play()
            self.musicx += 1

        if self.ship.health_death == True and self.musicy <= 1:
            self.m.play()
            self.m.set_volume(0.2)
            self.bgm.stop()
            
            self.musicy += 1

        for blook_pack in self.blookpacks:
            blook_pack.draw_bloodpacks()
        for minecraft_Launch in self.minecraftLaunchs.sprites():
            minecraft_Launch.draw_minecraftlaunch()
        for yuan_Launch in self.yuanlaunchs.sprites():
            yuan_Launch.draw_yuan()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        for bullet in self.alienbullets.sprites():
            bullet.draw_bullet()
        for bullet_left1 in self.alienbulletsleft1.sprites():
            bullet_left1.draw_bullet()
        for bullet_right1 in self.alienbulletsright1.sprites():
            bullet_right1.draw_bullet()
        for bullet_midtop2 in self.alienbulletsmidtop2.sprites():
            bullet_midtop2.draw_bullet()
        for bullet_left2 in self.alienbulletsleft2.sprites():
            bullet_left2.draw_bullet()
        for bullet_right2 in self.alienbulletsright2.sprites():
            bullet_right2.draw_bullet()
        for alien in self.alien_group.sprites():
            alien.draw_alien()
        for alien1 in self.alien_group1.sprites():
            alien1.draw_alien()
        for alien2 in self.alien_group2.sprites():
            alien2.draw_alien()
        for bomb in self.bombs:
            if bomb.visible:
                bomb.draw_bomb()

        if not self.game_active:
            self.play_button.draw_button()
            self.player_button.draw_button()
            self.player_button1.draw_button()

        if not self.ship.health_death and self.game_active:
            self.ship.blitme()
        if not self.ship1.health_death and self.game_active and self.player:
            self.ship1.blitme()
        #玩家1的分数和生命
        self.ship.prep_ships()
        self.ship.draw_health()
        #玩家2的分数和生命
        if self.player:
            self.ship1.prep_ships()
            self.ship1.draw_health()
        
        self._check_collide()
        self.ship_check_collide()
        self.alien_check_collide()
        #让屏幕可见
        pygame.display.flip()
        self.back_group.update()
        self.back_group.draw(self.screen)
    def _update_sprites(self):
        """更新精灵"""
        self.minecraftLaunchs.update()
        self.bullets.update()
        self.blookpacks.update()
        self.alienbullets.update()
        self.alienbulletsleft1.update()
        self.alienbulletsright1.update()
        self.alienbulletsmidtop2.update()
        self.alienbulletsleft2.update()
        self.alienbulletsright2.update()
        self.yuanlaunchs.update()
        if not self.ship.health_death:
            self.ship.update()
        if not self.ship1.health_death and self.player:
            self.ship1.update()

        self.alien_group.update()
        self.alien_group1.update()
        self.alien_group2.update()

    def run_game(self):
        while True:
            self._update_screen()
            if self.game_active:
                self._update_sprites()
            self._check_events()

            #控制屏幕帧率
            self.clock.tick(60)
            

                 
if __name__ == '__main__':
    run = AlienInvasion()
    run.run_game()
