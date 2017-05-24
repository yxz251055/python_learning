import pygame
from frame.settings import Settings
from frame.ship import Ship
import frame.game_functions as gf
from pygame.sprite import Group
from frame.game_stats import GameStats
from frame.button import Button

def run_game():

    #初始化游戏并创建一个屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width,ai_settings.screen_height)
    )
    pygame.display.set_caption("Alien Invasion")
    #创建play按钮
    play_button = Button(ai_settings,screen,"Play")

    #创建一个用于存储游戏统计信息的实例
    stats = GameStats(ai_settings)
    #创建一艘飞船
    ship = Ship(ai_settings,screen)

    #绘制一个用于存储子弹的编组
    bullets = Group()
    aliens = Group()
    #创建外星人群
    gf.create_fleet(ai_settings,screen,aliens,ship)
    #开始游戏的主循环
    while True:

        #监视键盘和鼠标事件
        gf.check_events(ship,ai_settings,screen,bullets,stats,play_button)
        if stats.game_active:
            #刷新飞船
            ship.update()
            #刷新子弹
            gf.update_bullet(ai_settings, screen,bullets,aliens,ship)
            #刷新外星人
            gf.update_aliens(ai_settings,stats,screen,aliens,ship,bullets)
        # 每次循环时都重绘屏幕
        gf.update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button)

run_game()