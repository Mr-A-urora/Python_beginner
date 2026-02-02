# 列表元素求和：计算给定列表中所有元素的和，但要跳过列表中的负数，numbers = [1, 2, -3, 4, -5, 6, 7, -8, 9]

numbers = [1, 2, -3, 4, -5, 6, 7, -8, 9]
total_sum = sum(num for num in numbers if num >= 0)
print(total_sum)
