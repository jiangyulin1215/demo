"""Jyl 代码编写"""
import prettytable as pt


def show_ticket(row_num):
    tb = pt.PrettyTable()
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    # print(tb.field_names)
    for item in range(row_num): # 遍历不用 int str float这些 只能是 list dic tuple set 以及 range()函数的方法
        lst = [f'第{item + 1}行', '有票', '有票', '有票', '有票', '有票']
        tb.add_row(lst)
    print(tb)


def order_ticket(row_num, row, column):
    tb = pt.PrettyTable()
    tb.field_names = ['行号', '座位1', '座位2', '座位3', '座位4', '座位5']
    print(tb)
    for item in range(row_num):
        if int(row) == item + 1:
            lst = [f'第{item + 1}行', '有票', '有票', '有票', '有票', '有票']
            lst[int(column)] = '已售'
            tb.add_row(lst)
        else:
            lst = [f'第{item + 1}行', '有票', '有票', '有票', '有票', '有票']
            tb.add_row(lst)
    print(tb)


if __name__ == '__main__':
    row_num = 13
    show_ticket(row_num)
    choose_num = input('请输入要选择的座位：（用逗号隔开）')
    try:
        row, column = choose_num.split(',')
    except:
        print('输入格式有误，注意逗号！')

    order_ticket(row_num, row, column)
