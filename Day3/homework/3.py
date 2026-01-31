""" names = 'yuan rain eric alvin'，引导用户输入一个名字，
判断是否在这个名字字符串中，是打印True，不是打印False"""

names = 'yuan rain eric alvin'

namelist = names.split()

choice = input('请输入您的名字:')

if choice in namelist:
	print(True)
else:
	print(False)
