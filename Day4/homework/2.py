""" 统计元音字母：编写一个程序，接受用户输入的一段文本，统计其中元音字母（a、e、i、o、u）的个数，并输出结果。"""

text = input("请输入一段文本：")

vowel_count = 0
for char in text:
    if char.lower() in ['a', 'e', 'i', 'o', 'u']:
        vowel_count += 1
    else:
        pass

print(f"元音字母的个数为：{vowel_count}")
