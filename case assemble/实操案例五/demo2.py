"""Jyl 代码编写"""
for item in range(1, 4):  # range()函数 ，参数（start,stop,step）,其中 start（默认 0 开始） 和 step （默认 步长为 1 ） 可以省略
    admin = input('请输入您的用户名：')
    pwd = input('请输入您的密码：')
    if admin == 'admin' and pwd == '8888':
        print('登录成功')
        break
    else:
        print('账号或密码错误，请重新输入')
        if item < 3:
            print(f'您还有{3 - item}次机会')
else:
    print('3次错误，账号密码已锁定，请联系后台')
