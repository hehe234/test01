"""
我们前面学习了while，在python除了while循环，还有一个经常使用的循环：for-in循环
语法：
for 迭代的变量 in 被循环的变量
"""
s="人工智能"
# 打印字符串的长度-> 也就是字符串内容的个数
print(len(s))
for item in s:
    print(item)

print('-'*50)

# 如果我们想获取被遍历对象的下标，我们可以使用  enumerate()函数
for index,item in enumerate(s):
    print(index,item)

print('-'*50)

# 设置enumerate的下标起始位置
for index,item in enumerate(s,start=100):
    print(index,item)