# 给定两个字典，找到它们共有的键存放到一个列表中
""" dict1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
dict2 = {'B': 20, 'D': 40, 'E': 50} """

dict1 = {'A': 1, 'B': 2, 'C': 3, 'D': 4}
dict2 = {'B': 20, 'D': 40, 'E': 50}

common_keys = [key for key in dict1 if key in dict2]
print("共有的键:", common_keys)
