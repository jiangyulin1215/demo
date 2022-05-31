"""Jyl 代码编写"""
import pygame
from pygame.sprite import Sprite


class Alien(Sprite):  # 与 子弹同理 继承Sprite类
    """表示创建单个外星人的类"""

    def __init__(self, ai_settings, screen):
        """"初始化父类Sprite"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        """加载外星人图像"""
        self.image = pygame.image.load("images/外星人.png")
        self.image = pygame.transform.scale(self.image, (100, 100))  # 利用位置参数，带 = 是关键字参数
        self.rect = self.image.get_rect()

        """初始化外星人图像位置"""
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        """存储外星人位置"""
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)

    def update(self):
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        """！！！速度设置好后，要时刻更新获取外接图形的位置！！！"""
        self.rect.x = self.x

    def check_edges(self):
        """"检测fleet是否在屏幕边缘，如果在的话就返回真值"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True
