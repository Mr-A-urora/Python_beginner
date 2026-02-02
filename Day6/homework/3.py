# 字典的乘积：计算给定字典中所有值的乘积：my_dict = {'A': 2, 'B': 3, 'C': 4, 'D': 5}

my_dict = {'A': 2, 'B': 3, 'C': 4, 'D': 5}
product = 1
for value in my_dict.values():
    product *= value
print("所有值的乘积:", product)
