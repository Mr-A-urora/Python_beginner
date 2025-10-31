name_list = ["高圆圆", "刘亦菲", "赵丽颖", "范冰冰", "李嘉欣"]

# 添加元素：append insert extend 
# （1）append：追加，向列表最后的位置添加元素
name_list.append("房东的猫")
print(name_list, len(name_list))

# （2）insert：插入
name_list.insert(0, "房东的猫")
print(name_list, len(name_list))

# （3）extend：扩展
new_name_list = ["福禄寿", "甜心格格"]
name_list.extend(new_name_list)
print(name_list, len(name_list))
