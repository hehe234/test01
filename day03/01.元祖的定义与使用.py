"""
在python中元祖使用()表示
元祖中的内容是固定的，不能被修改
创建元祖
a=(1,2,10)
a=("张三","李四","王五")
a=tuple("hell world") # 把字符串转换成元祖
元祖也可以使用for in 循环来遍历
"""
a=(1,2,5,8,10)
print(a)
# a=tuple("hello world") # 把字符串转换成元祖
# print(a)

# 循环遍历元祖中的成员
for i in a:
    print(i)

print("-"*50)

"""
元组是一个不可以被改变的列表
元组也是有下标的,下标(索引)都是从0开始的
	有下标就可以通过下标来进行获取
	元组不可以改变,只能获取
"""
# 通过下标获取元祖中的成员内容
print(a[0])
print(a[1])
print(a[2])
print("="*50)
# 元祖中的成员内容不能被修改
# a[0]=100
# print(a)
# 元祖中的成员内容不能被删除
# del a[0]
# print(a)

# 元组推导式与列表的推导式一样
# 需求：获取a元祖中的所有偶数，保存到一个新的元祖中
b=(item for item in a if item%2==0)
for item in b:
    print(item)