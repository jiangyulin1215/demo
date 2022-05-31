"""Jyl 代码编写"""


class Settins():  # 类名一般用大写首字母的方式
    """存储相关设置选项"""

    def __init__(self):  # __init__中有几个形参就传几个实参到实例对象中，类的调用只能通过实例对象来调用
        # 初始化屏幕设置
        """以下在类内 构造函数（初始化）中定义的变量，称为 实例变量； 在 __init__外，class Settings下定义的是 类变量；
        实例变量只能通过实例化对象后获取，类变量可以通过 Settings.类变量 的方式获取"""
        # self.ship_speed_factor = None
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # 飞船速度,是浮点数的小数
        self.ship_limit = 2

        # 关于子弹的设置
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # 外星人的设置内容
        self.fleet_drop_speed = 10

        # 加快游戏的节奏
        self.speed_scale = 1.1

        # 外星人点数的速度提高
        self.score_scale = 1.5
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        self.ship_speed_factor = 1.5
        self.bullet_speed_factor = 3
        self.alien_speed_factor = 1
        # fleet_direction 右移为 1 ， 左移 -1
        self.fleet_direction = 1

        self.alien_points = 50

    def increase_speed(self):
        self.ship_speed_factor *= self.speed_scale
        self.bullet_speed_factor *= self.speed_scale
        self.alien_speed_factor *= self.speed_scale
        self.alien_points = int(self.alien_points * self.score_scale)
        # print(self.alien_points)
