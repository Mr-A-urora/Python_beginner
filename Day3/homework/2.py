""" 有些程序经常需要引导用户输入“Y”或“N”，其中“Y”代表肯定，“N”代表否定。
无论用户输入大写的“Y”还是小写的“y”，结果都被视为肯定。肯定打印True。"""

Decision = input('请输入您的选择:')

if Decision.upper() == 'Y':
	print(True)
else:
	print(False)
