"""
    写入到json数据
        里面存储的是json格式的文件
        将数据写入到json文件中
        操作步骤：
            导包 => import json
            with open("json数据的文件名","参数",encoding="utf-8") as f:
                json.dumps(字典,参数,ensure_ascii=False)
        解释，参数说明
            with => 固定写法
            open => 打开JSON文件
            参数  =>
                w => write => 写入文件
                r => read  => 读取文件
                b => binary => 二进制
                encoding="utf-8" 防止json数据中有中文乱码，所以设置成utf-8
                as => 起别名
                ensure_ascii=False => 防止ascii的转换成unicode编码
"""
# 导包
import json
# 创建字典
# dict1={"username":"张三","age":18,"addr":"长沙","gender":"男"}
# # 写入json文件
# with open("data.json","w",encoding="utf-8") as f:
#     json.dump(dict1,f,ensure_ascii=False)
# print("数据写入完毕")

# 读取data.json文件，在控制台打印读取到的数据
with open("data.json","r",encoding="utf-8") as f:
    infomation=json.load(f)
print(infomation,type(infomation))