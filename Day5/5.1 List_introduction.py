name_list = ["高圆圆", "刘亦菲", "赵丽颖", "范冰冰", "李嘉欣"]

print(name_list, type(name_list))

print(name_list[1])
print(len(name_list))
print(name_list[1:4])

for name in name_list:
    if name.startswith("赵"):
        print(name)
