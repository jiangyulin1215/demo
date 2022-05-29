"""Jyl 代码编写"""


# stu_lst = []


class Student():
    def __init__(self, name, age, sex, score):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score

    def get_show(self):
        print(self.name, self.age, self.sex, self.score)


if __name__ == '__main__':
    print('请输入5位学员信息：（姓名#年龄#性别#分数）')
    lst = []
    for i in range(0, 5):
        s = input(f'请输入第{i + 1}位学生信息：')
        s_lst = s.split('#')
        # print(type(s_lst))
        # s_lst = s.strip("#") # 用错函数！ strip是去除前后空格！！！！
        # 创建学生对象
        stu = Student(s_lst[0], int(s_lst[1]), s_lst[2], int(s_lst[3]))
        lst.append(stu)

    # 遍历列表
    for item in lst:  # lst 是包含Student类的列表，遍历列表，可以将每个学生的信息单独调用出来，间接使用类类的get_show方法
        item.get_show()
