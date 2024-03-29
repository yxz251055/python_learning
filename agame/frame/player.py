import pygame

class PlayShip():

    def __init__(self,ai_settings,screen):
        '''初始化飞船并设置其初始化位置'''

        self.screen = screen
        self.ai_settings = ai_settings
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        #将每艘飞船放在屏幕底部中央
        self.rect.centerx = self.screen_rect.centerx
        self.rect.centery = self.screen_rect.centery

        #在飞船的属性center中存储小数值
        #center左右，bottom上下
        self.centerx = float(self.rect.centerx)
        self.centery = float(self.rect.centery)
        self.bottom = self.rect.bottom
        #移动标志
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

    def update(self):
        '''根据移动标志调整飞船的位置'''
        if self.moving_right:
            self.centerx += self.ai_settings.ship_speed_factor
            #往右不超过屏幕
            if self.rect.right > self.screen_rect.right:
                self.centerx -= self.ai_settings.ship_speed_factor
        if self.moving_left:
            self.centerx -= self.ai_settings.ship_speed_factor
            # 往左不超过屏幕
            if self.rect.left < self.screen_rect.left:
                self.centerx += self.ai_settings.ship_speed_factor
        if self.moving_up:
            self.centery -= self.ai_settings.ship_speed_factor
            # 往上不超过屏幕
            if self.rect.top < self.screen_rect.top:
                self.centery += self.ai_settings.ship_speed_factor
        if self.moving_down:
            self.centery += self.ai_settings.ship_speed_factor
            if self.rect.bottom > self.screen_rect.bottom:
                self.centery -= self.ai_settings.ship_speed_factor

        #根据self.center更新rect对象
        self.rect.centerx = self.centerx
        self.rect.centery = self.centery

    def blitme(self):
        '''在指定位置绘制飞船'''
        self.screen.blit(self.image,self.rect)