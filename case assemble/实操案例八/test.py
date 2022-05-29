"""Jyl 代码编写"""


def test(*args, **kwargs):
    # print(a)
    print(args)  # args 返回的是数量可变的位置参数,表现形式是 元组
    print(kwargs) # 返回的是 字典的键值对，表现形式是 字典



test(1, 3, 5, 7, c='2', d=4)
