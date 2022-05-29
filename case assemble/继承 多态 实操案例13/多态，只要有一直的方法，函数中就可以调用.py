"""Jyl 代码编写"""


class Instrument():
    def make_sound(self):
        pass


class Erhu(Instrument):  # 继承Instrument类
    def make_sound(self):  # 重写了 make_sound 方法
        print('二胡在演奏')


class Piano(Instrument):
    # super().__init__()
    def make_sound(self):
        print('钢琴在演奏')


class Violin(Instrument):
    def make_sound(self):
        print('小提琴在演奏')


class Bird():
    def make_sound(self):  # Bird类与Instrument没有关系，但是也有make_sound的方法，就可以使用play的函数，因为play函数中存在make_sound的方法
        print('小鸟在唱歌')


# 演奏的函数
def play(Instrument):
    Instrument.make_sound()


if __name__ == '__main__':
    play(Erhu())
    play(Piano())
    play(Violin())
    play(Bird())
