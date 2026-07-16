l1=[1,2,3,1]
l2=[4,5,6]
# + 可以将两个列表合并
print(l1+l2)
print("-"*50)
# * 可以将列表重复n次
print(l1*3)
print("-"*50)
# in 可以判断某个元素是否在列表中,not in 可以判断某个元素是否不在列表中
print(1 in l1)
print(1 not in l2)
print("-"*50)
print(l1.count(1))
print("-"*50)
print(l1.index(1))
print("-"*50)
l1.append(4)
print(l1)
print("-"*50)
l1.insert(0,0)
print(l1)
print("-"*50)
# 无返回值
l1.extend(l2)
print(l1)
print("-"*50)
l1.remove(1)
print(l1)
print("-"*50)
l1.reverse() # 翻转列表中的内容
print(l1)
# 获取列表中的最大值、最小值、长度
print(max(l1))
print(min(l1))
print(len(l1))
print("-"*50)

# 列表的排序
l3=[2,234,456,234,12,6,1]
print(sorted(l3)) # 升序排列
# reverse=True 降序排列
print(sorted(l3,reverse=True))