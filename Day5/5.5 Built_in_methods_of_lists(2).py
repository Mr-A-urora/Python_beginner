name_list = ["高圆圆", "刘亦菲", "赵丽颖", "范冰冰", "李嘉欣", "房东的猫", "甜心格格"]

# 删除元素：pop remove clear
# （1）pop：按索引删除
ret = name_list.pop(3)
print("被删除的内容为：" + ret)
print(name_list)

name_list.pop()   # pop()方法不传值默认删除最后一个
print(name_list)

# （2）remove：按内容删除
name_list.remove("刘亦菲")
print(name_list)

# （3）clear：清空列表
name_list.clear()
print(name_list)

# del命令：删除
del name_list   # 删除列表或者列表中的元素
# print(name_list)   #  已经删除列表，无法打印
