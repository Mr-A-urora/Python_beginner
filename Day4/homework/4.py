""" 身份证号码的倒数第二位数字是奇数，表示性别为男性，否则为女性，
引导用户输入身份证号，先判断是否为18位，再判断性别。"""

id_number = input("请输入身份证号码：")

if len(id_number) == 18 and int(id_number[16]) % 2 != 0:
    print("性别为男性")
elif len(id_number) == 18 and int(id_number[16]) % 2 == 0:
    print("性别为女性")
else:
    print("身份证号码位数不正确!")
