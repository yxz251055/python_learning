import sys
import pygame
from frame.bullet import Bullet
from frame.alien import Alien
from time import sleep


def check_events(ship, ai_settings, screen, bullets,stats,play_button):
    # 监视键盘和鼠标事件
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ship, ai_settings, screen, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x,mouse_y = pygame.mouse.get_pos()
            check_paly_button(stats,play_button,mouse_x,mouse_y)

def check_paly_button(stats,play_button,mouse_x,mouse_y):
    #点击play按钮时开始游戏
    if play_button.rect.collidepoint(mouse_x,mouse_y):
        stats.game_active = True

def check_keydown_events(event, ship, ai_settings, screen, bullets):
    # 向右移动飞船
    if event.key == pygame.K_RIGHT:
        ship.moving_right = True
    # 向左移动飞船
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    # 向上移动飞船
    elif event.key == pygame.K_UP:
        ship.moving_up = True
    # 向下移动飞船
    elif event.key == pygame.K_DOWN:
        ship.moving_down = True
    # 发射一枚子弹
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False
    elif event.key == pygame.K_UP:
        ship.moving_up = False
    elif event.key == pygame.K_DOWN:
        ship.moving_down = False


def update_screen(ai_settings,screen,stats,ship,aliens,bullets,play_button):
    # 更新屏幕上的图像，并切换到新屏幕
    screen.fill(ai_settings.bg_color)

    # 在飞船和外星人后面重绘所有子弹
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    ship.blitme()
    aliens.draw(screen)

    #游戏处于非活动状态，就绘制play按钮
    if not stats.game_active:
        play_button.draw_button()
    # 让最近绘制的屏幕可见
    pygame.display.flip()


def update_bullet(ai_settings, screen, bullets, aliens, ship):
    # 刷新子弹
    bullets.update()
    # 删除已消失的子弹
    for bullet in bullets.copy():
        if bullet.rect.top <= 0:
            bullets.remove(bullet)
    check_bullet_alien_collisions(ai_settings, screen, bullets, aliens, ship)


def check_bullet_alien_collisions(ai_settings, screen, bullets, aliens, ship):
    # 检查是否有子弹击中了外星人，如果有，则删除相应的子弹和外星人
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens) == 0:
        # 删除现有的子弹并创建一群新的外星人
        bullets.empty()
        create_fleet(ai_settings, screen, aliens, ship)


def fire_bullet(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullet_num:
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def create_fleet(ai_settings, screen, aliens, ship):
    """创建外星人群"""
    # 创建一个外星人并计算一行可容纳多少外星人
    # 外星人间距为外星人的宽度
    alien = Alien(ai_settings, screen)
    number_rows = get_number_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 创建外星人群
    for row_number in range(number_rows):
        number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width, row_number) - 3
        for alien_number in range(number_aliens_x):
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


# 计算一行可容纳多少外星人
def get_number_aliens_x(ai_settings, alien_width, row_number):
    available_space_x = ai_settings.screen_width - alien_width - (2 * alien_width * row_number)
    number_aliens_x = int(available_space_x / (2 * alien_width))
    return number_aliens_x


# 创建一个外新人并将其加入当前行
def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_number + (alien_width * row_number)
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


# 获取外星人下落的行数
def get_number_rows(ai_settings, ship_height, alien_height):
    available_space_y = (ai_settings.screen_height - ship_height)
    number_rows = int(available_space_y / (2 * alien_height))
    return number_rows


# 更新外星人
def update_aliens(ai_settings,stats,screen,aliens,ship,bullets):
    """检测外星人是否达边缘"""
    check_fleet_edges(ai_settings, aliens)
    aliens.update()
    #检测外星人和飞船之间的碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, aliens, ship, bullets)
        check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)
        #print("游戏结束！")


def check_fleet_edges(ai_settings, aliens):
    """有外星人到达边缘时采取措施"""
    for alien in aliens.sprites():
        if alien.check_edges():
            change_fleet_direction(ai_settings, aliens)
            break


def change_fleet_direction(ai_settings, aliens):
    """外星人群整体下移，并改变方向"""
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1

def ship_hit(ai_settings,stats,screen,aliens,ship,bullets):
    #相應被外星人撞到的飛船
    #將ships_left減1
    if stats.ships_left > 0:
        #stats.ships_left -= 1
        #清空外星人和子彈列表
        aliens.empty()
        bullets.empty()
        #創建一群新的外星人，并將飛船放到屏幕底端中央
        create_fleet(ai_settings,screen,aliens,ship)
        ship.center_ship()
        #暫停
        sleep(0.5)
        stats.game_active = False
    else:
        stats.game_active = False
        sys.exit()

def check_aliens_bottom(ai_settings,stats,screen,ship,aliens,bullets):
    """檢查是否有外星人到底端"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings,stats,screen,aliens,ship,bullets)
            break
