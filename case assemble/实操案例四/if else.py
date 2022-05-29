import random

price = random.randint(1000, 1500)
# print(f'今日价格为：{price}')
while True:
    guess_p = int(input('请输入您猜测的价位：'))
    if guess_p > price:
        print('大了，请重新输入')
    elif guess_p < price:
        print(('小了，请重新输入'))
    else:
        print('猜的帧准！')
        break

