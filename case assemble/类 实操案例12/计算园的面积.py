"""Jyl 代码编写"""

import math


class Circle(object):  # 类的首字母正常惯例是要 大写！！！！！！ 切记！！！
    def __init__(self, r):
        self.r = r

    def get_area(self):
        return math.pi * math.pow(self.r, 2)

    def get_perimeter(self):
        return 2 * math.pi * self.r


if __name__ == '__main__':
    r = int(input('请输入园的半径：'))
    c = Circle(r)
    print('圆的面积是:{:.2f}'.format(c.get_area()))
    print('圆的周长是:{:.2f}'.format(c.get_perimeter()))


