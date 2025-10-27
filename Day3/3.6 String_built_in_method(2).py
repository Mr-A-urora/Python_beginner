# （1）strip()：去除两端的空格或者换行符
name = "  HELLO   "
print(name, len(name))
ret1 = name.strip()
print(ret1, len(ret1))

a = "###Hello#####"
ret2 = a.strip("#")   # 去除左右两端的“#”号
ret3 = a.rstrip("#")   # 删除右边的“#”号
ret4 = a.lstrip("#")

print(ret2, len(ret2))
print(ret3, len(ret3))
print(ret4, len(ret4))

# (2) isdigit()：判断字符串是否为数字字符串
b = "hello"
c = "12"
d = "12h"
f = "12.4465"
print(b.isdigit())
print(c.isdigit())
print(d.isdigit())
print(f.isdigit())   # 浮点数也不行！

# （3）split()和join()
cities = "北京 哈尔滨 重庆 大连"
ret5 = cities.split(" ")
print(ret5, len(ret5))

ret6 = " ".join(ret5)
ret7 = ",".join(ret5)
print(ret6, len(ret6))
print(ret7, len(ret7))

info = "北京|哈尔滨|大连"
ret8 = info.split("|")
print(ret8, len(ret8), ret8[2])

# replace()：子字符串替换

cities_re = cities.replace(" ", ",")
print(cities_re, len(cities_re))

comments = "这个产品真棒！我非常喜欢。服务很差，不推荐购买。这个餐厅的食物质量太差了，味道不好。"
ret9 = comments.replace("差", "***").replace("不推荐", "***").replace("不好", "***")
print(ret9)

# （4）count:计算字符串中某个子字符串出现的次数
sentence = "PHP is the best language.PHP...PHP...PHP..."
ret10 = sentence.count("PHP")
print(ret10)
