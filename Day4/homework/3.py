# 计算1-2+3-4+......-1000最终的结果,能整除13的数不参与计算

result = 0

for i in range(1, 1001):
    if i % 13 == 0:
        continue
    elif i % 2 == 0:
        result -= i
    else:
        result += i

print(result)
