"""
break的作用是用于退出循环语句
"""
index = 1 # 初始化循环变量
while index <= 5: # 循环条件
    print(f"小明跑了第{index}圈")
    if index==3: # 当跑到第3圈的时候，就打印一句话，退出循环
        print("小明跑累了，不想跑了")
        break # 结束当前循环
    index += 1 # 迭代/改变循环变量初始值
print("程序执行完毕！！！")