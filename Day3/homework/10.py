""" 引导用户输入一个手机号，通过一个逻辑表达式判断该字符串是否符合电信手机号格式，
格式要求如下，是打印 True ,不是打印 False。
要求1：输入的长度必须是11位
要求2：输入内容必须全部是数字
要求3：前三位是133或153（电信号段）"""

phone = input("请输入手机号：")

if len(phone) == 11 and phone.isdigit() and phone[:3] in ['133', '153']:
    print(True)
else:
    print(False)
