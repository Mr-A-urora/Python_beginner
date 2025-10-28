# while循环之随机验证码
import random
import string

count = 0
result = ""

while count < 5:
    char = random.choice(string.ascii_letters + string.digits)
    result += char
    count += 1

print("verification code :", result)