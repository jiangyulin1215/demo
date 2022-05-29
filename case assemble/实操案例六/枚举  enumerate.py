"""Jyl 代码编写"""
year = [82, 89, 88, 86, 85, 00, 99]
print('原列表', year)
for index, value in enumerate(year):  # 内置类型 枚举 enumerate 可返回 索引值和元素值
    # print(index,value)
    if value != 0:
        # print("19" + str(year[index]))
        year[index]=int('19'+str(year[index]))
    else:
        # print('200' + str(year[index]))
        year[index]=int('200'+str(year[index]))
print('修改之后的列表:', year)

# 列表的排序
year.sort()
print(year)
# 倒叙
year.sort(reverse=True)
print(year)
