"""Jyl 代码编写"""
'''try except else finally'''
score = int(input('请输入分数：'))

if 0 <= score <= 100:
    print('分数为{}'.format(score))
else:
    raise Exception('分数不正确')  # !!!!!!raise 函数 手动抛出异常内容！！！！

