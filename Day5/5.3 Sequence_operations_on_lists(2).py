name_list = ["高圆圆", "刘亦菲", "赵丽颖", "范冰冰", "李嘉欣"]

# （1）成员判断
print("刘亦菲" in name_list)

# （2）拼接 + 
s1 = "我喜欢"
s2 = "赵丽颖"
print(s1 + s2)

# （3）列表循环：列表作为容器对象，可以通过for循环进行遍历
for name in name_list:
	print(name)
	
# （4）计算列表的元素个数：len
print(len(name_list))
