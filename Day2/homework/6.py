"""判断一个年份year是否是闰年
如果是，则打印“year是闰年”,否则打印“year不是闰年”
闰年满足以下条件：能被4整除但不能被100整除，或者能被400整除"""

year = int(input('请输入年份:'))

if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
	print('year是闰年!')
else:
	print('year不是闰年!')
