"""Jyl 代码编写"""


class GameStats():
    """跟踪游戏的统计信息"""

    def __init__(self, ai_settings):
        # self.ships_left = None  # 用添加吗？？？
        self.ai_settings = ai_settings
        self.reset_stats()
        self.game_active = False

        # 任何情况下都不重置最高分
        self.heigh_score = 0

    def reset_stats(self):
        """初始化游戏进行可能变化的参数"""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0  # 实例方法中的参数
        self.level = 1


