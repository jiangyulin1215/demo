"""Jyl 代码编写"""
"""猜数游戏"""
import random


def guess(num, guess_num):
    if num == guess_num:
        return 0
    elif guess_num > num:
        return 1
    else:
        return -1


num = random.randint(0, 100)
for item in range(10):
    guess_num = int(input('请输入要猜测的数字：'))
    result = guess(num, guess_num)
    if result == 0:
        print('猜对了')
    elif result == 1:
        print('大了')
    else:
        print('小了')
else:
    print('10次都没猜中')
