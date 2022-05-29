# 使用print进行输出的实操案例

"""一。使用Print方式进行输出，（输出的目的地是文件）"""
fp = open('D:/临时文件夹/Test.txt', 'a+')  # a+ 为读写模式，也可以用'w'为只读模式  指定了文件路径
print('奋斗成就更好的你！', file=fp)
fp.close()

"""二.使用文件的读写操作"""
with open('D:/临时文件夹/Test.txt', 'a') as file:  # 'a' 代表追加模式，不会重写之前写过的文件 ，指定了文件路径
    file.write('奋斗成就更好的我！')

filename = 'test2.txt'
with open(filename, 'w', encoding='utf-8') as wfile: # 未指定路径，默认在本文件内生成，记得要指定 编码模式utf-8以防止中文乱码
    wfile.write('奋斗成绩更好的你我他！')

