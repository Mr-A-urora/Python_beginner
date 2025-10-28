""" 打印出从 1 到 100 的所有整数，
将整除 3 的数字打印为 “Fizz”，
整除 5 的数字打印为 “Buzz”，
同时整除 3 和 5 的数字打印为 “FizzBuzz”。"""
for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(f"{i}:FizzBuzz")
    elif i % 5 == 0:
        print(f"{i}:Buzz")
    elif i % 3 == 0:
        print(f"{i}:Fizz")
    else:
        print("i =", i)