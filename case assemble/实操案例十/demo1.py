"""Jyl 代码编写"""
import math


def calcu(a, b, op):
    if op == '+':
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b != 0:
            return a / b
        elif b == 0:
            print('除数不能为0')


"""def div(a, b):
    if b != 0:
        return a / b
    elif b == 0:
        print('除数不能为0')"""


if __name__ == '__main__':
    a = int(input('请输入第一个整数：'))
    b = int(input('请输入第二个整数：'))
    op = input('请输入运算符：')
    print(calcu(a, b, op))
