"""Jyl 代码编写"""


def is_tango(a, b, c):
    if a < 0 and b < 0 and c < 0:
        raise Exception('三条边不能是负数')  # raise Exception,与下面语句非并列关系

    if (a + b) > c and (a + c) > b and (b + c) > a:
        print('是三角形')
    else:
        raise Exception('不能构成三角形')


if __name__ == '__main__':
    try:
        a = int(input("请输入第一个数:"))
        b = int(input("请输入第二个数:"))
        c = int(input("请输入第三个数:"))
    except Exception as e:
        print(e)
    else:
        is_tango(a, b, c)
