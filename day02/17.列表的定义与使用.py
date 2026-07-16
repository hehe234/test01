"""
python中的列表使用 [] 表示
列表的作用：用于保存不同的数据类型的多个值
特点：他有下标，可以保存重复的元素内容，可以修改、删除、添加元素

列表的定义
a=[] # 创建一个空列表
b=[1,2,3,'a','b'] # 创建列表的同时，向列表中添加元素
"""
a=[] # 创建一个空列表
b=[1,2,3,'a','b'] # 创建列表的同时，向列表中添加元素
print(a)
print(b)

# 打印列表的长度
print(len(a))
print(len(b))

# 向a列表中添加新的成员
a.append("张三")
a.append("李四")
a.append("王五")
print(a)
print(len(a))
# 在指定位置追加新的成员
a.insert(1,"赵六") # 第一个参数是下标位置，第二个参数是添加的成员
print(a)

# 通过下标去访问列表中的成员
print(a[2])
# 获取列表的最后一个成员
print(a[len(a)-1])
# 修改列表中成员的内容
a[0]="张无忌"
print(a)

# 删除列表中的成员
# del a[1]
# a.remove("赵六")
# print(a)

# 通过for循环来遍历列表中的所有成员
for index,i in enumerate(a):
    print(f"{index}-->{i}")

# 删除整个列表
del a
print(a) # 删除整个列表之后该变量名就不能使用来，报错信息： name 'a' is not defined