# 编写程序，找到给定列表中的所有大于平均值的元素并计算他们的总和

numbers = [10, 20, 30, 40, 50]

average = sum(numbers) / len(numbers)
above_average_numbers = [num for num in numbers if num > average]
total_sum = sum(above_average_numbers)

print(f"大于平均值的元素有: {above_average_numbers}")
print(f"这些元素的总和是: {total_sum}")
