"""
continue的作用：跳过本次循环，进入到下一次循环
"""
index = 1 # 初始化循环变量
while index <= 5: # 循环条件
    print(f"小明跑了第{index}圈")
    if index==3: # 当跑到第3圈的时候，就打印一句话，退出循环
        print("小明这一圈跑累了，休息下跑下一圈了")
        continue # 结束当前循环
    index += 1 # 迭代/改变循环变量初始值
print("程序执行完毕！！！")