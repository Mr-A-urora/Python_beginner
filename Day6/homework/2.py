# 给定一个字典，找到字典中值最大的键：my_dict = {'A': 10, 'B': 5, 'C': 15, 'D': 20}

my_dict = {'A': 10, 'B': 5, 'C': 15, 'D': 20}
max_key = max(my_dict, key=my_dict.get)
print(f"值最大的键是: {max_key}，对应的值是: {my_dict[max_key]}")
