# 编写一个程序， 统计给定列表中每个元素出现的次数，并将结果存储在一个字典中

my_list = [1, 2, 3, 2, 1, 3, 4, 5, 2, 1]
count_dict = {}

for item in my_list:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1

print(count_dict)
