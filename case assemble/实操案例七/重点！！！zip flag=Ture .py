"""Jyl 代码编写"""

constellation = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '摩羯座', '水瓶座', '双鱼座']
feature = ['积极乐观', '固执内向', '圆滑世故', '多愁善感', '迷之自信', '精明计较', '犹豫不决', '阴暗消极', '放荡不羁', '务实本分', '作天作地', '安于现状']

"""目的：将两个列表转成 集合，会用到一个函数 !!!  zip  !!!!,已经多次看到了zip，需要注意！"""

# a = zip(constellation, feature)
d = dict(zip(constellation, feature))
print(d)
key = input('请输入您要查询的星座:\n')
flag = True
for item in d:
    # 对字典的遍历会提炼出 key值(星座)，不会提炼出 value值（星座特点）
    # print(item)
    if key == item:  # 会先 遍历 全部内容后，将内容全部提取出来后与输入值做比较，输入的白羊座与遍历的白羊座都在第一位所以无误，但从金牛座开始 有白羊座在前，会按key值多少提示 else错误
        flag = True
        print(key, '对应的值为：', d.get(key))  # 字典用 get 获取显示值！！！！！！！！ 切记
        break
    else:
        flag = False
        # print('输入有误，请重新输入')

if not flag:
    print('对不起，您的输入有误')