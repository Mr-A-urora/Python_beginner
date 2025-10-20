# 布尔类型
a = True
b = False

print(type(a))
print(type(b))

age = 12
print(age > 18)
print(type(age > 18))

# bool() 获取某个值的布尔状态
print(bool(1))
print(bool(-1))
print(bool("中国"))
print(bool("0"))
print(bool(0))
print(bool(""))
print(bool([]))
print(bool({}))

# 零值：在Python中，每一个数据类型中有且只有一个零值，即布尔状态为false的值
# 整型和浮点型的零值就是0
# 字符串的零值就是“”(None)
# 列表的零值就是[]   字典的零值就是{}
