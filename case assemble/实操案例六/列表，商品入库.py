"""Jyl 代码编写"""
lst = []
for i in range(0, 5):
    # print(i)
    product = input('请输入商品编号和名称进行入库登记,每次只能输入一件商品:\n')
    lst.append(product)
print(lst)
print('----------------------------------------------------------------')
s_car = []
'''for index, value in enumerate(lst, 1001):
    goods = input('请输入要购买的商品编号：')
    if index == int(goods):
        s_car.append(lst[index-1001])
        continue
    elif str(goods) == 'q':
        print('您购物车里的物品为:\n {}'.format(s_car))
        break
    else:
        print('输入有误')
        continue'''
while True:
    goods = input('请输入您要购买的商品编号：')
    for item in lst:  # List里面是字符串类型， item里面 就也是 字符串类型 ，所以可用 find
        if item.find(goods) != -1:
            s_car.append(item)
            break  # 退出的是for

    if goods == 'q':
        break  # 退出的是while
print('您购物车里的商品为：')
# for m in s_car: # 需要逆序输出
#     print(m)
for fb in range(len(s_car) - 1, -1,-1):  # 因为是要到 0 ，所以 stop值为 -1  额外需要注意 倒叙要添加 步长！！！
    print(fb)
