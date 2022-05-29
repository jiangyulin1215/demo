"""Jyl 代码编写"""
# 模拟手机通讯录
phones = set()  # 集合是无序排序输出！！！！！！！！！！！！！！！！！！！！！！
# print(type(phones))
print(dir(set))
for item in range(5):
    info = input(f'请输入第{item+1}个联系人：')
    phones.add(info)
for i in phones:
    print(i)
