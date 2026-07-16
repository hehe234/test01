"""
在python中定义字典使用{}
字典使用键值对的形式，例如：
{"username":"张三","age":18,"addr":"长沙","gender":"男"}
username -> 键名  "张三"-> 值
"age"   -> 键名   18  ->   值
...

字典可以用于转换成JSON格式的数据，用于做前后端数据交互

字典也是一种数据类型,但是字典里面存储的是 key_value 值的形式
	一般别人会把数据转换JSON字符串,传递给我们,但是我们没有办法直接使用,所以我们一般将JSON字符串转换成一种数据结构,让我们利用python来进行操作,这种数据结构就叫做字典
字典用 {} 来进行表示
	() -> 元组
	[] -> 列表
	{} -> 字典
字典的key_value形式
	{key:value}
	注意: key是一个字符串双引号的形式
"""
dict1={"username":"张三","age":18,"addr":"长沙","gender":"男"}
print(dict1,type(dict1))
# 字典的增删改查操作
# 字典中添加新的成员
dict1["height"]=180
print(dict1)
# 修改字典中成员的值
dict1["username"]="张无忌"
print(dict1)
# 删除字典中成员
del dict1["username"]
print(dict1)
# 获取字典中的成员对应的值
print(dict1["addr"])

# 获取字典中的所有键名
keys=dict1.keys()
print(keys)
# 循环遍历keys，获取每个键名对应的值
for key in keys:
    # print(f"键名：{key},值：{dict1[key]}")
    # print(f"key：{key} --> value：{dict1[key]}")
    # 字典的get方法，传入键名获取值，如果键名不存在，则返回None
    print(f"key：{key} --> value：{dict1.get(key)}")

# 获取字典中的所有值
values=dict1.values()
print(values)