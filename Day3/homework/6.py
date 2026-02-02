"""输入一个三位数。将其拆分为百位数，十位数和个位数，并输出它们的和"""

number = input("请输入一个三位数: ")
if len(number) == 3 and number.isdigit():
    hundred = int(number) // 100
    ten = (int(number) % 100) // 10
    unit = int(number) % 10

    result = hundred + ten + unit

    print('{}的百位数是{}，十位数是{}，个位数是{}，它们的和是{}'.format(number, hundred, ten, unit, result))
else:
    print('输入的数字有误，请确认后重新输入！')
