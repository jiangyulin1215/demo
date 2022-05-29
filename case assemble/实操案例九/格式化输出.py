"""Jyl 代码编写"""
def get_show(lst):
    for item in lst:
        # print(item)
        for i in item:
            print(i, end='\t\t')
        print()

lst = [['01', '电风扇', '美的', 500],
       ['02', '洗衣机', 'TCL', 600],
       ['03', '微波炉', '老板', 1000],
       ]
print('编号\t\t名称\t\t\t品牌\t\t单价')
get_show(lst)

s = '格式化输出'
print(s.center(30, '-'))
for item in lst:
    item[0] = '000' + item[0]
    item[3] = '￥{:.2f}'.format(item[3])
get_show(lst)