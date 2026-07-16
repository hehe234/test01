"""
in 指的是 a 被 b 是否包含，如果包含就返回True,否则就返回False
not in 指的是 a 不被 b 是否包含，如果b不包含a就返回True,否则就返回False
"""
a="晴朗"
b="今天天气好晴朗，处处好风光！"
c="雨天"
if a in b:
    print(f"b 中包含 {a} 内容")
else:
    print(f"b 中不包含 {a} 内容")
print("="*50)

if c not in b:
    print(f"b 中不包含 {c} 内容")
else:
    print(f"b 中包含 {c} 内容")