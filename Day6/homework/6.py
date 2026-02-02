# 对列表元素先去重再排序：l = [1, 12, 1, 2, 2, 3, 5]

l = [1, 12, 1, 2, 2, 3, 5]
unique_sorted_list = sorted(set(l))
print(unique_sorted_list)
