"""
字符串的常用属性和方法
+ 拼接内容
* 字符串重复的次数
upper() 字母转换成大写
lower() 字母转换成消协
split() 切割字符串，返回的是一个列表
index() 找到字符内容第一次出现的对下标
strip() 去除字符串左右两端的空格
count() 统计某个字符出现的次数
len() 统计字符串的长度
startswith() 判断字符串是否以 xx 开头
endswith() 判断字符串是否以 xx 结尾
replace(old,new) 替换字符串中的内容
"""
s="  hell World  "
# print(s+"hello")
# print(s*3)
# print(s.upper())
# print(s.lower())
# print(s.split("l"))
# print(s.count("l"))
# print(s.index("l"))
# print(s.find("l")) # 查找字符串中字符出现的位置
# print(s.startswith("  h"))
# print(s.endswith("d  "))
# print(s.strip())
print(s.replace("l","L"))