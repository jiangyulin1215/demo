"""Jyl 代码编写"""
import sys
import pygame
from ship import Ship
from alien import Alien
from bullet import Bullet
import settings
from time import sleep
from game_stats import  GameStats

def check_keydown_events(event, ai_settings, screen, ship, bullets):  # 形参和实参位置一定要对应，否则会报 Atrribute 错误！！，否则可使用关键字参数
    if event.key == pygame.K_RIGHT:  # event 是 Pygame.event.get(）的遍历结果，需要传入
        ship.moving_right = True  # ship 是Ship类的实例化对象，需要传入
    elif event.key == pygame.K_LEFT:
        ship.moving_left = True
    elif event.key == pygame.K_SPACE:
        fire_bullet(ai_settings, screen, ship, bullets)
    elif event.key == pygame.K_q:
        sys.exit()


def fire_bullet(ai_settings, screen, ship, bullets):
    """如果检测到子弹消失以后，再创建新的子弹编组"""
    if len(bullets) < ai_settings.bullets_allowed:  # 利用内置函数 len() 统计bullets数组的长度 ！！！
        # 创建一个子弹，加入编组bullets中
        new_bullet = Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def check_keyup_events(event, ship):
    if event.key == pygame.K_RIGHT:
        ship.moving_right = False
    elif event.key == pygame.K_LEFT:
        ship.moving_left = False


def check_events(ai_settings, screen, ship, bullets):  # 满足函数小写并用下划线连接的要求
    """响应键和鼠标的事件监控"""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, ai_settings, screen, ship, bullets)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, ship)

    '''elif event.type == pygame.KEYDOWN:
        # 函数中的形参加入 ship,ship 在 alien_invasion中是Ship类的实例对象，用ship来调用飞船类中 置于中间位置的属性
        if event.key == pygame.K_RIGHT:
            ship.moving_right = True  # 如果是真值就一直移动
        elif event.key == pygame.K_LEFT:
            ship.moving_left = True
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_RIGHT:
            ship.moving_right = False  # 标记为假时就停止移动
        elif event.key == pygame.K_LEFT:
            ship.moving_left = False'''


def update_screen(ai_settings, screen,stats, ship, aliens, bullets):  # 更新屏幕
    # 填充屏幕颜色，绘制飞船，screen,ai_setting,ship 作为形参传进函数，调用的时候就不用额外赋值
    screen.fill(ai_settings.bg_color)
    ship.blitme()
    # alien.blitme()
    aliens.draw(screen)
    for bullet in bullets.sprites():
        bullet.draw_bullet()
    # 如果游戏处于非活动状态，就执行按键
    if not stats.game_active:
        play_button.draw_button()


    # 目的 让屏幕一直出现
    pygame.display.flip()


def update_bullets(ai_settings, screen, ship, aliens, bullets):  # 子弹更新的函数，以讲话alien_invasion的主函数
    bullets.update()
    for bullet in bullets.copy():  # 对子弹的 浅拷贝 ！！！！
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)  # 对 原 子弹 抵达y轴0点后进行删除
    # print(len(bullets))
    check_alien_bullet_collisions(ai_settings, screen, ship, aliens, bullets)


def check_alien_bullet_collisions(ai_settings, screen, ship, aliens, bullets):
    """子弹和外星人的碰撞"""
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)  # sprite.groupcollide（）方法 可以检测两个列表，碰撞后删除
    if len(aliens) == 0:
        create_fleet(ai_settings, screen, ship, aliens)


def get_number_aliens_x(ai_settings, alien_width):
    available_space_x = ai_settings.screen_width - 2 * alien_width
    number_aliens_x = available_space_x // (2 * alien_width)
    return number_aliens_x


def get_number_aliens_rows(ai_settings, ship_height, alien_height):
    available_space_y = ai_settings.screen_height - 3 * alien_height - ship_height
    number_aliens_rows = available_space_y // (2 * alien_height)
    return number_aliens_rows


def create_alien(ai_settings, screen, aliens, alien_number, row_number):
    """需计算屏幕一行的宽度(要留边)，以及一行能容纳多少外星人"""
    alien = Alien(ai_settings, screen)
    alien_width = alien.rect.width
    # 创建一个外星人并将其加入当前行
    alien = Alien(ai_settings, screen)
    alien.x = alien_width + 2 * alien_width * alien_number
    alien.rect.x = alien.x
    alien.rect.y = alien.rect.height + 2 * alien.rect.height * row_number
    aliens.add(alien)


def create_fleet(ai_settings, screen, ship, aliens):  # 创建外星人群组 """要么就在函数内定义变量，要么就在函数声明时定义形参变量""
    """创建外星人群"""
    alien = Alien(ai_settings, screen)
    number_aliens_x = get_number_aliens_x(ai_settings, alien.rect.width)  # 对 函数‘get_number_aliens_x（）'返回值的调用
    numbers_row = get_number_aliens_rows(ai_settings, ship.rect.height, alien.rect.height)
    # 创建第一行外星人
    for row_number in range(numbers_row):
        for alien_number in range(number_aliens_x):
            # 创建一个外星人并将其加入当前行
            create_alien(ai_settings, screen, aliens, alien_number, row_number)


def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    check_fleet_edges(ai_settings, aliens)
    aliens.update()

    # 检测外星人是否与飞船碰撞
    if pygame.sprite.spritecollideany(ship, aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)

    # 检查外星人是不是到了底部
    check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets)


def check_fleet_edges(ai_settings, aliens):
    for alien in aliens.sprites():  # 用 item或者其它也都可以，但是推荐用 alien 教材里是用alien
        if alien.check_edges():
            chang_fleet_direction(ai_settings, aliens)
            break


def chang_fleet_direction(ai_settings, aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_drop_speed
    ai_settings.fleet_direction *= -1  # 不用 * 是否可以？ 不行，带 * 可以改变是 1  还是 -1


def ship_hit(ai_settings, stats, screen, ship, aliens, bullets):
    """响应被外星人撞到的飞船"""
    if stats.ships_left > 0:
        # 将ship_left 减 1
        stats.ships_left -= 1

        # 情况外星人列表和子弹夹
        aliens.empty()  # empty函数是sprite包里的函数
        bullets.empty()

        # 创建一群新的外星人并置飞船于中间
        create_fleet(ai_settings, screen, ship, aliens)
        ship.center_ship()
        # 暂停
        sleep(0.8)
    else:
        stats.game_active = False


def check_aliens_bottom(ai_settings, stats, screen, ship, aliens, bullets):
    """检查是否有外星人到了屏幕底部"""
    screen_rect = screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            # 像飞船被撞到一样处理
            ship_hit(ai_settings, stats, screen, ship, aliens, bullets)
            break
