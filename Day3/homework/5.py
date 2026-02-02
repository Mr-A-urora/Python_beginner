"""用户输入一个11位手机号,将第5位至第8位替换成 * """

number = input("请输入一个11位手机号: ")

if len(number) == 11 and number.isdigit():
    final_number = number[:4] + '****' + number[8:]
    print('替换后的手机号为:{}'.format(final_number))
else:
    print('输入的手机号有误，请确认后重新输入！')
