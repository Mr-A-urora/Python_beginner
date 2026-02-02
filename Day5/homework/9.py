# 编写程序，计算给定列表中所有正数元素的平均值

numbers = [10, -2, 33, -45, 50, 6, -1, 23]
positive_numbers = [num for num in numbers if num > 0]
if positive_numbers:
    average = sum(positive_numbers) / len(positive_numbers)
    print(f"正数元素的平均值是: {average}")
