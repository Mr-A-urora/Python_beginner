""" 引导用户输入一个双值加法字符串,例如3+5或3 + 5,计算出两个数字的和,打印出来"""

user_input = input("请输入一个双值加法字符串: ")
user_input = user_input.strip()

if "+" in user_input:
    and_values = user_input.split("+")

    number1 = and_values[0].strip()
    number2 = and_values[1].strip()

    result = int(number1) + int(number2)
    print('{}和{}的和是{}'.format(number1, number2, result))
else:
    print('输入内容有误，请确认后重新输入！')
