""""进制转换！"""


def fun():
    num = int(input('请输入一个十进制整数：'))  # input返回的是一个 str
    print(num, '的二进制是：', bin(num))  # 第一种写法
    print(str(num) + '的二进制是' + bin(num))  # 第二种写法，bin类型不用额外转成str
    print('%s的二进制数是：%s' % (num, bin(num)))  # 第三种，格式化字符串
    print('{}的二进制是：{}'.format(num, bin(num)))  # 第三种，格式化字符串
    print(f'{num}的二进制是：{bin(num)}')  # 第三种，格式化字符串
    print('{:-^60}'.format(''))

    print('%s 的 八进制是： %s' % (num, oct(num)))
    print(f'{num}的八进制是:{oct(num)}')

    print('{:-^60}'.format(''))
    print('%s 的 十六进制是： %s' % (num, hex(num)))
    print(f'{num}的十六进制是{hex(num)}')


if __name__ == '__main__':
    while True:
        try:
            fun()
            break
        except:
            print('程序出错，请重新输入')

