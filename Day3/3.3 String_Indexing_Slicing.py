s = "Hello 中国！"

# (1)索引的语法：字符串对象[索引]
print(s[6], type(s[6]))
print(s[-1])

# (2)切片的语法：字符串索引[开始索引:结束索引]
print(s[1:6])
print(s[1:7])
print(s[1:9])
print(s[1:10])   # 不建议！
# 缺省
print(s[1:])
print(s[:6])
print(s[:])
# 负索引
print(s[-4:-1])
print(s[5:8])
print(s[5:-1])

# (3)切片的语法：字符串索引[开始索引:结束索引:步长 = 1]

print(s[::1])   # step = 1: 从左向右一个个取
print(s[::3])

print(s[::-1])   # step = -1: 从右向左一个个取

print(s[3:0:-1])
print(s[3:0])
print(s[0:3])
