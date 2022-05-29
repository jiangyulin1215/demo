"""预测子女身高"""
m_height = float(input('请输入父亲身高：'))
f_height = float(input('请输入母亲身高：'))
c_height = (m_height + f_height) * 0.54
print(f'子女的身高可估计为：{c_height}')
