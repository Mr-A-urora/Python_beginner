# 浅拷贝的几种情况：
# （1）使用切片操作符[:]进行拷贝
l1 = [1, 2, 3, 4, 5]
l = l1[:]
print(l)
print(id(l1), id(l))
print(id(l1[2]), id(l[2]))

# （2）使用list()函数进行拷贝
l2 = [1, 2, 3, 4, 5]
l = list(l2)
print(l)

# （3）使用copy()方法进行拷贝（需要导入copy模块）
l3 = [1, 2, 3, 4, 5]
l = l3.copy()
print(l)

# 深拷贝实现：
import copy
l4 = [1, 2, 3, [4, 5]]
l = copy.deepcopy(l4)
print(l)
l[3][0] = 400
print(l4)
print(l)
