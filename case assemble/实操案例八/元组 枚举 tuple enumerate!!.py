"""Jyl 代码编写"""


caffe = ('蓝山', '卡布奇诺', '拿铁', '摩卡', '玛奇朵')

# print(type(caffe))
# print(dir(tuple))
print('你好！欢迎光临小马咖啡屋')
print('本店经营的咖啡有')
# print('    '.join(caffe))
    # record=input('请输入您喜欢的编号：')
for key ,value in enumerate(caffe,1):  # 枚举将下标从 1 开始显示，但实际下标值还是从 0 开始
    print(key,value,end=' ')

key = int(input('\n请输入您喜欢的编号：'))
if 0<=key<=len(caffe):
    print(f'您的{caffe[key-1]}好了，请取走')