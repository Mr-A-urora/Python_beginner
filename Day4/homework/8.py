""" 猜数字游戏
1.首先，程序使用random.randint函数产生一个1~10之间的随机数。
2.然后，程序通过for循环提示玩家输入一个猜测的数字，玩家可以输入一个1~10之间的整数。
3.如果玩家猜对了数字，程序输出恭喜玩家的信息并结束游戏；如果玩家猜错了，程序会根据玩家输入的数字与随机数之间的大小关系来提示玩家是否猜对，并在每次猜错后告诉玩家还剩下几次机会。
4.如果玩家在三次机会内猜对了数字，程序输出恭喜玩家的信息并结束游戏；否则程序输出很遗憾的信息并结束游戏。"""

import random
random_number = random.randint(1, 10)
max_attempts = 3

for attempt in range(1, max_attempts + 1):
    guess = int(input("请输入你猜的数字（1-10）："))
    
    if guess == random_number:
        print("恭喜你，猜对了！")
        break
    elif guess < random_number:
        print(f"你猜的数字太小了！你还有 {max_attempts - attempt} 次机会。")
    else:
        print(f"你猜的数字太大了！你还有 {max_attempts - attempt} 次机会。")

else:
    print(f"很遗憾，你没有在 {max_attempts} 次机会内猜对数字。正确答案是 {random_number}。")
