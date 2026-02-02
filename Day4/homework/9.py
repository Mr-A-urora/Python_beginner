# 打印一个n * n的矩阵，每个元素的值等于其所在行数和列数之和。

n = int(input("请输入矩阵的大小n："))

for i in range(n):
    for j in range(n):
        print(i + j, end='\t')
    print()
