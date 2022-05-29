"""Jyl 代码编写"""
"""二分搜索法， 折半算法 
mid=(start + end) // 2
小了：新start= 原mid + 1
大了：新end = 原mid -1
"""
import random

num = random.randint(1, 100)
# while True:
for i in range(1, 11): # 要从1开始算，如果从 0 开始默认的话会少算一次
    guess_n = int(input('请输入您猜测的数字:'))
    if guess_n > num:
        print('大了')

    elif guess_n < num:
        print('小了')
    else:
        print('真厉害！')
        print(f'您一共猜测了{i}次')
        break
