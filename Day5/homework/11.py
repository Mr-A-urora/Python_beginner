# 给定一个列表，找出列表中任意两个元素之间的最大差值和最小差值

numbers = [10, 3, 6, 1, 8, 15, 4]
max_diff = max(numbers) - min(numbers)
min_diff = float('inf')

for i in range(len(numbers)):
    for j in range(i + 1, len(numbers)):
        diff = abs(numbers[i] - numbers[j])
        if diff < min_diff:
            min_diff = diff

print(f"最大差值: {max_diff}")
print(f"最小差值: {min_diff}")
