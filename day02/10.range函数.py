"""
range() 函数 也是可以循环遍历的,可以传入不同个数的参数
range(n)传入一个参数，只是的从0到n-1，例如：range(3) -> 0,1,2
range(n,m)传入两个参数，是从n开始到m-1
range(n,m,k)传入三个参数，是从n开始到m-1结束，每次步长为k
"""
r1=range(3) # 0,1,2
r2=range(10,16) # 10,11,12,13,14,15
r3=range(0,10,3) #0 3 6 9

# 使用循环来遍历r1
for i in r1:
    print(i)
print("-"*50)

# 使用for循环来遍历r2
for i in r2:
    print(i)
print("-"*50)

# 使用for循环来遍历r3
for i in r3:
    print(i)
print("-"*50)