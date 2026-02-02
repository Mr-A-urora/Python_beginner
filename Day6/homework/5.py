# 编写程序，将两个字典合并，并将相同键对应的值进行加法运算。
"""dict1 = {'A': 1, 'B': 2, 'C': 3}
dict2 = {'B': 10, 'D': 20, 'C': 30}"""

dict1 = {'A': 1, 'B': 2, 'C': 3}
dict2 = {'B': 10, 'D': 20, 'C': 30}

merged_dict = dict1.copy()

for key, value in dict2.items():
    if key in merged_dict:
        merged_dict[key] += value
    else:
        merged_dict[key] = value

print("合并后的字典:", merged_dict)
