"""Jyl 代码编写"""

import sys
import pygame
import game_function as gf  # 模块名也要用下划线连接，方便导入
from settings import Settins  # 导入settings模块中的Settings类
from ship import Ship
from alien import Alien
from bullet import Bullet
from pygame.sprite import Group
from game_stats import GameStats
from button import Button
from scoreboard import Scoreboard


def run_game():  # 函数的定义一般使用小写  ’单词_单词‘的形式，类 用首字母字母大写
    # 初始化游戏并创建一个窗口
    pygame.init()
    ai_settings = Settins()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))  # 元组形式，可以 ctrl + 鼠标 参考方法说明
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings, screen, stats)
    pygame.display.set_caption('Alien Invasion')
    play_button = Button(ai_settings, screen, 'Play')
    ship = Ship(ai_settings, screen)  # 实例化对象，用以实现Ship类功能
    bullets = Group()  # 创建子弹的编组
    aliens = Group()
    # alien = Alien(ai_settings,screen)  # 创建一个外星人的实例   2 . 有了外星人群后不再需要
    gf.create_fleet(ai_settings, screen, ship, aliens)

    while True:
        # 监视键盘和鼠标事件,调用game_function中的 check_events 函数，将功能写在其它模块，本模块只做实现用
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            # 飞船移动
            ship.update()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb, screen, ship, aliens, bullets)

        # 绘制屏幕内的相关信息，填充颜色，绘制飞船，外星人，子弹等，刷新屏幕
        gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


if __name__ == '__main__':
    run_game()
