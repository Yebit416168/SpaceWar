import pygame.font


class Scoreboard:
    """分数类"""
    def __init__(self,ai_game):
        """显示得分的属性"""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = ai_game.settings
        self.score = 0
        self.high_score = 0
        self.font = pygame.font.Font("font\\Minecraft.ttf", 16)
        self.score_image = self.font
        self.high_score_image = self.font
        self.exp_level = 0
        self.score_level = 500                                   
        self.launch = 0
        self.minecraft_launch = 2000
        self.yuanlaunch = 0
        self.yuanlaunch_launch = 1000
        self.diffculty_score = 1000
        self.diffculty_level = 0
        self.bullet = 1 
        self.bullet3 = 500

        #得分图形
        self.prep_score()  
        self.prep_high_score()
        self.prep_diffculty()

    def prep_diffculty(self):
        """渲染难度"""
        diffculty_str = f"难度等级:{self.settings.diffculty}"
        self.diffculty_image = self.font.render(diffculty_str,True,(255,255,255), None)
        #右上角显示难度
        self.diffculty_rect = self.diffculty_image.get_rect()
        self.diffculty_rect.right =self.screen_rect.right
        self.diffculty_rect.top = 20

    
    def prep_score(self):
        """渲染分数"""
        round_score = round(self.score,-1)
        score_str = f"分数:{round_score:,}"
        self.score_image = self.font.render(score_str,True,(255,255,255), None)
        
        #右上角显示分数
        self.score_rect = self.score_image.get_rect()
        self.score_rect.right =self.screen_rect.right
        self.score_rect.top = 0

    def prep_high_score(self):
        """渲染分数"""
        high_score = round(self.high_score,-1)
        high_score_str = f"最高分:{high_score:,}"
        self.high_score_image = self.font.render(high_score_str,True,(255,255,255), None)

        self.high_score_rect = self.high_score_image.get_rect()
        self.high_score_rect.centerx = self.screen_rect.centerx
        self.high_score_rect.top = 0
    
    def show_score(self):
        """绘制得分"""
        self.screen.blit(self.score_image,self.score_rect)
        self.screen.blit(self.high_score_image,self.high_score_rect)
        self.screen.blit(self.diffculty_image,self.diffculty_rect)
        

