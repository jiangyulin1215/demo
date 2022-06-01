"""Jyl 代码编写"""

import pygame
from pygame.sprite import Sprite

"""类是对客观世界和思维世界存在的规律在计算机中的反应，封装称了一套大体的 模板， 可以创建多个
以此 类 为基础的 实例化对象， 类有属性和方法，在类内编写的正式实现对象操作的一系列方法，不建议在 类的模块
内进行 打印或输出，而是可以通过其它模块来调用此类的模块，进行输出"""


class Ship(Sprite):
    def __init__(self, ai_settings, screen):  # __init__中有几个形参，在实例化对象中就要传几个实参，这个Ship类的实例化对象中，要额外传个screen
        super(Ship,self).__init__()
        """初始化飞船，并设置其位置"""
        self.screen = screen
        self.ai_settings = ai_settings

        # 加载飞船图像并获取其外接矩形
        # 除了传参以外，构造函数中也可以  定义其它的实例变量
        self.image = pygame.image.load('images\shiboat.png')
        self.image = pygame.transform.scale(self.image, size=(80, 80))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # 将飞船放在底屏中间
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        self.center = float(self.rect.centerx)

        # 移动标志，使飞船持续移动，用 Ture 和 False 方式来标记开过，使 默认使False，让飞船不动
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """让飞船在屏幕上居中"""
        self.center = self.screen_rect.centerx

    def update(self):
        """根据移动标志真或假，调整飞船位置"""
        if self.moving_right and self.rect.right < self.screen_rect.right:  # 如果self.moving_right为真值时，飞船‘一直’向右移动
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:  # 同理, 两个判断条件，1，当为True时飞船移动 2. 左边界大于0时飞船才移动
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center

    def blitme(self):  # 类内方法
        """在指定位置绘制飞船图形"""
        self.screen.blit(self.image, self.rect)

