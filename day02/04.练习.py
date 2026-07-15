# 利用循环来求1~50之间的和
"""
需求： 1+2+3+...+48+49+50
可以通过循环来遍历  1,2,3,4...,5=48,49,50
定义一个变量用于保存每次累加之和
sum = 0 # 初始值为0
"""

index = 1  # 初始化循环变量
sum = 0  # 初始化变量保存每次累加的和
while index <= 50:
    # print(index)
    sum += index # sum = sum + index
    index += 1

print(f"sum = {sum}")
