"""
在python中，如果需要转换变量的数据类型可以使用
    将变量转换成整数类型  => int(变量名)
    将变量转换成小数类型  => float(变量名)
    将变量转换成布尔类型  => bool(变量名)
    将变量转换成字符串类型  => str(变量名)

特殊情况：
    当我们把数字0转换成布尔类型的时候，得到的结果就是 False
    当我们把None转换成布尔类型的时候，得到的结果就是 False
    当我们把空字符串("")转换成布尔类型的时候，得到的结果就是 False
    当我们把数字1转换成布尔类型的时候，得到的结果就是 True
"""

num1=0
num2=1
str1=""
a=None
print(bool(num1))
print(bool(num2))
print(bool(str1))
print(bool(a))