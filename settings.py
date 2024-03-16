class Settings:
    def __init__(self):

        #子弹速度
        self.ship_speed = 2.5

        #子弹设置
        self.bullet_speed  = 6.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullets_allowed = 20

        #难道系数
        self.diffculty = 0


        #外星人速度
        self.max_alien_speed = 3 + self.diffculty
        self.min_alien_speed = 2
        
