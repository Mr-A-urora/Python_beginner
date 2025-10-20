# %占位符
"""name = "中国"
age = 18
height = 180

s = '''
员工信息：
姓名：%s
年龄：%d
身高：%s
''' % (name, age, height)
print(s)"""

# f-str
"""name = "中国"
age = 18
height = 180.115268

# 前方可添加填充符号。<:左对齐，>:右对齐，^居中对齐
s = f"姓名：{name:*^15}，年龄：{age:^2}，身高：{height:<6.5}"   # 格式{变量名:宽度.精度}
print(s)

name = "相信自己"
age = 22
height = 185.152368

s = f"姓名：{name:@^14}，年龄：{age:^2}，身高：{height:<6.5}"
print(s)"""


