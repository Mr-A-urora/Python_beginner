# 判断一个学生的考试成绩score是否在80到100之间（包括80和100）

score = int(input('你的成绩为:'))

if score in range(80, 101):
	print('Yes!')
else: 
    print('No!')
