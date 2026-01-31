# 假设有一个变量count的初始值为0，将count增加5次，每次增加值分别为1，2，3，4，5，然后打印count的值

count = 0

for i in range(1, 6):
	count += i
	
print('count的输出值为:{}'.format(count)) 
