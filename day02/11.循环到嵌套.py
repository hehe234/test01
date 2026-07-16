"""
需求：我们要在控制台输出4行，每行有5个星星
*****
*****
*****
*****
分析：
每一行有5个星星，总共有4行
拆解步骤：
我们来打印一行的5个星星
print("*"),我们来打印5次
"""
# 第一行的5列=>5个星星
# print("* ",end="") # end="" 不换行
# print("* ",end="")
# print("* ",end="")
# print("* ",end="")
# print("* ",end="")
# print() # 换行
#
# # 第二行的5列=>5个星星
# print("* ",end="")
# print("* ",end="")
# print("* ",end="")
# print("* ",end="")
# print("* ",end="")
# print() # 换行
#
# # 第三行的5列=>5个星星
# print("* ",end="")
# print("* ",end="")
# print("* ",end="")
# print("* ",end="")
# print("* ",end="")
# print() # 换行
#
# # 第四行的5列=>5个星星
# print("* ",end="")
# print("* ",end="")
# print("* ",end="")
# print("* ",end="")
# print("* ",end="")
# print() # 换行

# 使用一个循环，来输出4行5列
# for i in range(4): # 0,1,2,3
#     print("* ", end="")
#     print("* ", end="")
#     print("* ", end="")
#     print("* ", end="")
#     print("* ", end="")
#     print()  # 换行

# 使用两个循环，来输出4行5列 => 循环的嵌套,口诀【心法】：外层循环控制行，内层循环控制列
for i in range(4): # 0,1,2,3
    for j in range(5): # 0,1,2,3,4
        print("* ", end="") # 输出*，不用换行，只有当内层循环全部执行完毕后，才执行外层循环的print()方法，换行
    print() # 换行
print("="*50)
"""
需求：使用循环嵌在控制台实现如下效果
*               第一行一个*
* *             第二行两个*
* * *           第三行三个*
* * * *         第四行四个*
* * * * *       第五行五个*
"""
for i in range(5): # 0,1,2,3,4  外层循环控制行
    for j in range(i+1): # 内层循环控制列
        print("* ",end="") #内层循环的循环体，输出 *  不换行
    print() # 换行


