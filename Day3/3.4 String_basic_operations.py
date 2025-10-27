# （1）len()
a = "Hello 中国！"
print(len(a))
print(a[len(a)-1])

print(len([1, 2, 3]))
print(len({"v1":"k1"}))

# （2）拼接 + *
b1 = "Hello"
b2 = "中国"
b3 = "!"

b = b1 + " " + b2 +b3
print(b)

print("*" * 10 + b2)

# （3） in 返回布尔值
print("l" in b1)
print("h" in b1)
print("h" not in b1)
