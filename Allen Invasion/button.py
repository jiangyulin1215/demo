"""Jyl 代码编写"""

import pygame.font  # pygame中的字体


class Button():
    def __init__(self, ai_settings, screen, msg):
        """初始化按键属性"""
        # self.ai_settings = ai_settings
        # self.msg_image_rect = None
        # self.msg_image = None
        self.screen = screen
        self.screen_rect = screen.get_rect()

        # 设置按键尺寸和其它属性
        self.width, self.height = 500, 300
        self.button_color = (170, 60, 18)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 80)

        # 创建按键的rect对象，并居中
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center

        # 按钮标签
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.button_color, self.msg_image_rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
