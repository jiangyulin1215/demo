'''计算BMI值'''

heigh = float(input('请输入你的身高：'))
weight = float(input('请输入你的体重：'))
BMI = weight / (heigh + weight)
print('你的BMI值为：{:0.2f}'.format(BMI))
