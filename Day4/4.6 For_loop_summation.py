# For循环案例之随机验证码
# while循环之随机验证码
import random
import string

result = ""

for i in range(0, 5):
    char = random.choice(string.ascii_letters + string.digits)
    result += char

print("verification code :", result)
