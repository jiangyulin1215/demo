"""Jyl 代码编写"""
import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """继承 Sprite类，主要是应用其编组功能"""

    def __init__(self, ai_settings, screen, ship):
        super(Bullet, self).__init__()
        self.screen = screen  # 需要在屏幕上创建一个子弹，首先初始化一下屏幕

        # 在（0，0）处创建一个子弹矩形，再设置正确的位置
        self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
        self.rect.centerx = ship.rect.centerx  # ai_settings 和 ship 作为类内方法中需要引入的实例对象要传入Bullet类内的初始化__init__中
        self.rect.top = ship.rect.top

        # 用小数存储子弹位置
        self.y = float(self.rect.y)

        self.color = ai_settings.bullet_color
        self.speed_factor = ai_settings.bullet_speed_factor

    def update(self):
        """向上移动子弹位置"""
        # 更新子弹位置的小数值
        self.y -= self.speed_factor

        # 更新子弹位置
        self.rect.y = self.y

    def draw_bullet(self):
        # 在屏幕上绘制子弹
        pygame.draw.rect(self.screen, self.color, self.rect)
