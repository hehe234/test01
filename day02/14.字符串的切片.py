"""
字符串的切片：就是我们说的截取内容
语法：
字符串变量名[开始,结束,步长]
s1="hello world"
s2=s1[1,5]  => ello
"""

s1="hello world"
#   012345678910
print(s1[1:5]) # ello
print(s1[1:8:2]) # el o
print(s1[:5]) # hello
print(s1[6:]) # world
print(s1[:]) # hello world
print(s1[::2]) # hlowrd
# 有负数
print(s1[:-2]) # hello wor
print(s1[-5:-2]) # wor

print(s1[::-1]) # dlrow olleh 翻转字符串内容
print(s1[::-2]) # drwolh 翻转字符串内容每次跳2截取
