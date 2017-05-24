class Settings():
    '''存储《外星人入侵》的所有设置的类'''

    def __init__(self):
        '''初始化游戏的设置'''
        #屏幕设置
        self.screen_width = 630
        self.screen_height = 870
        self.bg_color = (240,255,255)

        #飞船的设置
        self.ship_speed_factor = 1
        self.ship_limit = 3

        #设置外星人移动速度
        self.alien_speed_factor = 1
        self.fleet_drop_speed = 10
        #1表示向右，-1表示向左
        self.fleet_direction = 1

        #设置子弹
        self.bullet_speed_factor = 1.5
        self.bullet_width = 10
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_num = 3