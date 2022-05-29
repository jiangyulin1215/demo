"""Jyl 代码编写"""


def fun():
    count = 0
    ch = input('请输入要统计的字符：')
    sentence = input('请输入要检查的内容：')
    flag = False
    for item in sentence:
        if ch.upper() == item or ch.lower() == item:
            flag = True
            count += 1
        else:
            flag = False
            # print('无对应字符')
            # break

    if not flag:
        return count


print(fun())

'''老师的写法'''


def get_count(s, ch):
    count = 0  # 赋一个初始化值
    for item in s:
        if ch.lower() == item or ch.upper() == item:
            count += 1
    return count


if __name__ == '__main__':
    ch = input('请输入要统计的字符：')
    s = 'hello python Hellocpp hellojango'
    count = get_count(s, ch)
    print(f'{ch}在{s}中d的统计结果为:', count)
