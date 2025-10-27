"""勇士与地下城
（1）怪物房：遇到了史莱姆。
    1. 选择攻击，战胜史莱姆，则经验加20，金币加20，失败则经验减20，金币减20，血值减20，成功的概况为50%。
    2. 选择逃跑，则金币减20。
（2）宝箱房：你打开了宝箱，获得了钥匙。
（3）陷阱房：你触发了陷阱，受到了毒箭的伤害，血值减 10。
（4）商店：你来到了商店，打印当前血值和金币，一个金币买一个药水对应 10 个血值，引导是否购买药水。
    1. 购买，引导购买几个金币的药水，并完成减金币和增血值。
    2. 不购买，打印退出商店。"""

import random

coin = 100
exp = 100
blood = 100
chest = []

room = input("请选择房间：")

if room == "怪物房":
    print("遇到了史莱姆")
    choice = input("【1.攻击 / 2.逃跑】")
    if choice == "1":
        # 攻击
        print("选择战斗！")
        is_win = random.choice([1, 2])
        if is_win == 1:
            print("战胜史莱姆！")
            coin += 20
            exp += 20
        else:
            print("没打过，被史莱姆打趴！")
            coin -= 20
            exp -= 20
            blood -= 20
    elif choice == "2":
        # 逃跑
        print("逃跑ing")
        coin -= 20
    else:
        print("无效输入！")
    print("离开了怪物房！")
elif room == "宝箱房":
    print("你打开了宝箱，获得了钥匙")
    chest.append("钥匙")
    print(f"当前宝贝：{chest}")
elif room == "陷阱房":
    print("你触发了陷阱，受到了毒箭的伤害")
    blood -= 10
elif room == "商店":
    print(f"玩家的金币：{coin},血值：{blood}")
    print("一个金币买一个药水对应10个血值")
    decision = input("是否购买药水【Y/N】")
    if decision == "Y":
        num = int(input("购买几瓶药水？"))
        coin -= num
        blood += 10 * num
        print(f"当前玩家的金币：{coin}, 血值：{blood}")
    elif decision == "N":
        print("退出商店！")
    else:
        print("无效输入！")
print(f"""
玩家信息：
    金币：{coin}
    经验值：{exp}
    血值：{blood}
""")
print("游戏结束！")
