gf = {"name":"高圆圆", "age":32}

#（1）修改和添加：字典对象.update(字典对象)
gf.update({"age":27})
print(gf)
gf.update({"height":175})
print(gf)

#（2）删除键值对
ret = gf.pop("age")
print(ret)
print(gf)

#（3）查看键值 get()
name = gf.get("name")
print(name)
age = gf.get("ages")   # 当键不存在的时候，默认返回None
print(age)

# 如果可以匹配到相关键，则返回相关键的信息，否则返回第二个参数相关内容
name = gf.get("name", "匿名用户")
print(name)
name = gf.get("names", "匿名用户")
print(name)

#（4）查看所有的键和值
keys = gf.keys()
print(keys, type(keys))
print(list(keys)[0])

values = gf.values()
print(values, type(values))
print(list(values)[0])

items = gf.items()
print(items, type(items))
print(list(items)[0])

# eg:遍历字典
for i, j in gf.items():
	print(i, j)

#（5）创建字典
courses = ["English", "Math", "Chinese"]
ret = dict.fromkeys(courses, 60)
print(ret)
