"""
什么是三元/目运算符
三元运算符其实也就是 if-else的简写版本
语法：
    操作1 if bool else 操作2
说明：看 bool的值是True还是False,如果是True,那么就执行 操作1，如果是False就执行 操作2
"""
a=10
b=20
c= a+b if a<b else a-b
print(f"c = {c}")

d= a+b if a>b else a-b
print(f"d = {d}")
