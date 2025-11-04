t = ("yuan", 18, "185cm")
print(type(t))

# 索引和切片
t1 = (11, 22, 33, 44, 55)
print(t1[3])
print(t1[1:4])
print(t1[::-1])

# 元组只可读，不可进行修改操作
"""t1[2] = 333
print(t1)"""

# 计算长度
print(len(t1))

# 内置方法只有两个：count和index
print(t1.count(33))
print(t1.index(44))

# 其他基本操作
# in
print("33" in t1)

# 拼接 +
t2 = (1, 2)
t3 = (3, 4)
print(t2 + t3)

# 遍历元素
for i in t1:
    print(i)

# 补充：元组中若只有一个数据，则要在后面添加一个逗号，否则数据类型不会被认为是元组
t4 = (1)
print(type(t4))
t5 = (1,)
print(type(t5))
