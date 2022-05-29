"""Jyl 代码编写"""


def find_answer(question):
    with open('taobao.txt', 'r',encoding='utf-8') as file:
        while True:
            line = file.readline()
            if not line:  # if line== '' 到文件末尾退出
                break

            # 字符串分割 split
            keyword = line.split('|')[0]  # 问题
            reply = line.split('|')[1]  # 回复
            if keyword in question:
                return reply
    return False

if __name__ == '__main__':
    question = input('Hi，你好，小蜜在此等主人很久了，有什么烦恼快和小蜜说吧：')
    while True:
        if question == 'bye':
            break
        reply = find_answer(question)
        if not reply:
            question=input('小蜜不知道里在本茨什么，请说文档有关内容：')
        else:
            print(reply)
            question=input('小主，你可以咨询文档txt内的相关内容哦：')
    print('小主再见')