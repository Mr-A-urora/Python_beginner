""" s = 'hello world'。
（1）通过正反索引切片world
（2）获取world的翻转，即'dlrow'"""

s = 'hello world'

s1 = s[6:11]
print('正向索引切片:{}'.format(s1))

s2 = s[-5:]
print('反向索引切片:{}'.format(s2))

s3 = s[10:5:-1]
print('world的翻转为:{}'.format(s3))

