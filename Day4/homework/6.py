# 编写一个程序，生成斐波那契数列的第20个数字（斐波那契数列是指从0和1开始，后面的每一项都是前两项的和）

first = 0
second = 1
count = 2

while count < 20:
    third = first + second
    first = second
    second = third
    count += 1

print(second)
