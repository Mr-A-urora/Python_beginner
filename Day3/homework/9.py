""" 引导用户输入一个字符串，保证长度一定是 4 的倍数，不足位补 = """

strs = input('请输入字符串：')

count = 4 - (len(strs) % 4)

if count != 4:
    strs += '=' * count
else:
    pass

print(strs)
