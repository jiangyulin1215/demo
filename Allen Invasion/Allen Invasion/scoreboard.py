"""Jyl 代码编写"""
import pygame.font
from pygame.sprite import Group
from ship import Ship


class Scoreboard():
    """得分信息"""

    def __init__(self, ai_settings, screen, stats):
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.ai_settings = ai_settings
        self.stats = stats

        self.text_color = (0, 0, 0)
        self.font = pygame.font.SysFont(None, 48)

        self.prep_score()
        # self.prep_score()
        self.prep_heigh_score()
        self.prep_level()
        self.prep_ship()

    def prep_score(self):
        """得分渲染成图像"""
        rounded_score = int(round(self.stats.score, -1))
        score_str = "Score:{:,}".format(rounded_score)
        self.score_image = self.font.render(score_str, True, self.text_color, (250, 235, 215))

        self.score_rect = self.score_image.get_rect()
        self.score_rect.right = self.score_rect.right + 900  # 教程是 screen_rect,我用的是自己图形的外接矩形获取
        self.score_rect.top = self.score_rect.top + 20

    def prep_heigh_score(self):
        """"将最高分单独渲染保存"""
        heigh_score = int(round(self.stats.heigh_score, -1))
        heigh_score_str = "Heighest Score:{:,}".format(heigh_score)
        self.heigh_score_image = self.font.render(heigh_score_str, True, self.text_color, (255, 228, 225))

        # 最高分的板子显示
        self.heigh_score_rect = self.heigh_score_image.get_rect()
        # self.score_rect.centerx = self.score_rect.centerx
        self.heigh_score_rect.centerx = self.heigh_score_rect.centerx + 350  # 教程是 screen_rect,我用的是自己图形的外接矩形获取
        self.heigh_score_rect.top = self.heigh_score_rect.top + 20

    def prep_level(self):
        """等级渲染成图像"""
        self.level_image = self.font.render("Level:" + str(self.stats.level), True, self.text_color, (135, 206, 235))
        # 放在 Score 下面显示
        self.level_rect = self.level_image.get_rect()
        self.level_rect.right = self.level_rect.right + 900
        self.level_rect.top = self.level_rect.top + 65

    def show_score(self):
        """在屏幕上显示得分"""
        self.screen.blit(self.score_image, self.score_rect)
        self.screen.blit(self.heigh_score_image, self.heigh_score_rect)
        self.screen.blit(self.level_image, self.level_rect)
        self.ships.draw(self.screen)  # 编组才能调用 draw ,  正常都是 pygame里 blit

    def prep_ship(self):
        """显示剩余飞船"""
        self.ships = Group()
        for ship_number in range(self.stats.ships_left):
            ship = Ship(self.ai_settings, self.screen)  # 在方法中定义的类，需要有 实例参数
            ship.rect.x = 10 + ship_number * ship.rect.width  # 设置显示剩余飞船的大小
            ship.rect.y = 10
            self.ships.add(ship)
