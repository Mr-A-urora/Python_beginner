num = [10, 2, 34, 4, 5, 2]

# （1）sort:对元素的大小排序
num.sort()   # 从小到大排序
print(num)

# （2）reverse:翻转
num.reverse()
print(num)

# 拓展：sorted。教程为入门教程，此处不做过多介绍。

# （3）index:查询某元素的索引值
print(num.index(5))

# （4）count：计算某元素出现的个数
n = num.count(34)
print(n)
