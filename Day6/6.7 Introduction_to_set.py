# 集合的元素值必须是不可变数据类型
s1 = {1, 2, 3}
print(type(s1), len(s1))

# （1）无序性

# （2）唯一性
s2 = {1, 2, 3, 3, 3, 3}
print(s2)

# 面试题：将列表去重
l = [1, 2, 3, 3, 4]
print(list(set(l)))

# （3）可变类型：字典和列表
# 内置方法：添加和删除
s3 = {1, 2, 3}
s3.add(4)
s3.update({2, 3, 4, 5})
print(s3)

s3 = {1, 2, 3, 4, 5, 6}
s3.remove(2)   # remove()删除元素不存在的时候会报错
print(s3)
s3.discard(3)   # discard()删除元素不存在的时候什么也不发生
s3.discard(33)
print(s3)
s3.pop()   # pop()随机删除元素
print(s3)
s3.clear()   # clear()清空集合内容
print(s3)
