# 判断用户名密码是否正确

Username = '2735594368'
Password = 'Zj15352382068'

Username_input = input('请输入您的账号:')
Password_input = input('请输入您的密码:')

if Username_input == Username and Password_input == Password:
		print('欢迎!')
elif Username_input != Username:
	print('帐号错误!请检查之后,重新输入您的帐号!')
else:
	print('密码错误,请检查之后,重新输入您的密码!')
