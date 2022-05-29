"""Jyl 代码编写"""
""""显示中超球队的前5名，元组中包含元组"""
scors = (("广州恒大", 72), ("北京国安", 70), ("上海上港", 66), ("江苏苏宁", 53), ("山东鲁能", 51))
for key, value in enumerate(scors, 1):  # 字典 和 枚举类型都可以遍历两个 # 特别重要！！！！！！
    print(key, end='   ')  # end=''遍历以后可以横排显示
    for sccor in value:
        print(sccor, end=" ")
    print( )