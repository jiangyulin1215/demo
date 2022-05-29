"""Jyl 代码编写"""
print(ord('a'))  # ord（） 内置函数， 可查询字符对应的码位， chr() 与其相反,知道码位后得出对应字符

'''第一种方法 for in 语句'''
x = 97
for _ in range(1, 27):  # 可用 _ 代替变量，代表只是循环次数，不用叠加变量
    print((chr(x), '--->', x))
    x += 1
'''for item in range(1, 27):
    item += 96
    print(chr(item))'''

print('------------------------------------------')

"""第二种方法, while 语句"""
# 97+26 = 123
while x < 123:
    print(chr(x), '=======', x)
    x += 1
