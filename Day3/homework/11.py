""" 引导用户输入一个邮箱格式字符串，比如 916852314@163.com 或 1052065088@qq.com 等，
然后将邮箱号和邮箱类型名打印出来,比如邮箱号916852314和163邮箱"""

email = input("请输入邮箱地址：")

email_num, email_type = email.split('@')
email_type, email_else = email_type.split('.')

print(f"邮箱号：{email_num}，邮箱类型：{email_type}邮箱")
