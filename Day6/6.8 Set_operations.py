s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

# 方式一：操作符 交集（&） 差集（-） 并集（|）
print(s1 & s2)
print(s2 & s1)
print(s1 - s2)
print(s2 - s1)
print(s1 | s2)
print(s2 | s1)

# 方式二：集合的内置方法
print(s1.intersection(s2))
print(s2.intersection(s1))

print(s1.difference(s2))
print(s2.difference(s1))

print(s1.symmetric_difference(s2))   # 对称差集
print(s2.symmetric_difference(s1))

print(s1.union(s2))
print(s2.union(s1))
