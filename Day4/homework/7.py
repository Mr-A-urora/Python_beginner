""" 编写一个程序，接受用户输入的一个整数，判断该数是否是素数（只能被1和自身整除的数）。
注意，素数的定义是大于1的自然数，只能被1和自身整除，没有其他的正因数。"""

num = int(input("请输入一个整数："))

if num > 1:
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            print(f"{num} 不是素数")
            break
    else:
        print(f"{num} 是素数")
