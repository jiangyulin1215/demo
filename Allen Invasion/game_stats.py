"""Jyl 代码编写"""


class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        self.ships_left = None # 用添加吗？？？
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = True

    def reset_stats(self):
        self.ships_left = self.ai_settings.ship_limit  # 飞船总数
