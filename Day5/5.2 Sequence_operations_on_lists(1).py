name_list = ["高圆圆", "刘亦菲", "赵丽颖", "范冰冰", "李嘉欣"]

# 一、索引操作：
# （1）查看元素：列表对象[索引]，获取元素，重点是获取的只有一个元素值
print(name_list[1])
print(name_list[-1])

# （2）修改元素：列表对象[索引] = 值
name_list[3] = "佟丽娅"
print(name_list)

# 二、切片操作：
# （1）查看多个元素：列表对象[开始索引:结束索引:步长]，获取多个值的子列表
print(name_list[2:])
print(name_list[::-1])
print(name_list[-4:-2:1])
print(name_list[-2:-4:-1])

# （2）修改多个元素：
name_list[1:4] = ["霹雳狐", "小允", "小苏菲"]
print(name_list)
