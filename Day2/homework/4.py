# 输入一个数字，判断是否是三位数且能被13整除

num = int(input('请输入数字:'))

if num % 13 == 0:
	if num // 100 in range (1, 10):
		print('Yes!')
	else:
		print('No!')
else:
	print('No!')
