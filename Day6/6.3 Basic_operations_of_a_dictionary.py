gf = {"name":"高圆圆", "age":32}

# 无序，属于容器类型
print(len(gf))

# 增或改：字典对象[键] = 值
gf["age"] = 27
print(gf)
gf["height"] = 175
print(gf)

# 删除
del gf["age"]
print(gf)

# 查看键值
print(gf["name"])   # 键不存在会报错

# 成员判断 in
print("names" in gf)
print("height" in gf)

# 遍历字典所有的键值对
for key in gf:
	print(key, gf[key])

# Python 字典中键（key）的名字不能被修改，我们只能根据键（key）修改值（value）
