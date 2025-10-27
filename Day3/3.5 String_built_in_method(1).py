# （1）upper()和lower()
a = "Hello World!"
s1 = a.upper()
s2 = a.lower()
print(s1)
print(s2)

# （2）startswith()和endswith()，返回布尔值
print(a.startswith("H"))
print(a.startswith("He"))
print(a.startswith("h"))
print(a.endswith("d!"))

# （3）find()和index()，查找某子字符串的索引
print(a.find("l"))
print(a.index("l"))
print(a.find("H"))
print(a.index("H"))
print(a.find("h"))   # 查找不到返回-1
# print(a.index("h"))   # 查找不到会报错
