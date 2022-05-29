"""Jyl 代码编写"""
import time


def show_info():
    print('输入提示的数字，执行相应操作，0为退出，1为查看登录日志')


def write_log(usrname):  # 有传实际参数的要求的时候，一般都会把形参写在括号内，这样就不用赋初始值
    with open('log.txt', 'a', encoding='utf-8') as file:
        s = f'用户名是{usrname},登录时间{time.strftime(" %Y- %m-%d  %H:%M:%S", time.localtime(time.time()))}\n'
        file.write(s)


def read_log():
    with open('log.txt', 'r', encoding='utf-8') as file:
        while True:
            line = file.readline()
            if line == '':
                break
            else:
                print(line)


if __name__ == '__main__':
    usrname = input('请输入用户名：')
    pwd = input('请输入密码:')
    if usrname == 'admin' and pwd == 'admin':
        print('登录成功')
        write_log(usrname)  # 记录登录
        show_info()
        num = int(input('请输入操作数字：'))
        while True:
            if num == 0:
                print('退出成功')
                break
            elif num == 1:
                print('查看登录日志')
                read_log()
                num = int(input('请输入操作数字：'))

            else:
                print('输入有误，请重新输入')
                show_info()
                num = int(input('请输入操作数字：'))
    else:
        print('用户名或密码错误')

        '''print(time.time()) #得到的是秒
        print(time.localtime(time.time()))
        print(time.strftime('%Y-%m-%d    %H:%M:%S',time.localtime(time.time())))'''
