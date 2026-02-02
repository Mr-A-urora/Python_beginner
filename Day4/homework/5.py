""" 计算初始本金为1万，年利率为0.0325的情况下，需要多少年才能将本金和利息翻倍，
即本金和利息的总和达到原来的两倍。"""

principal = 10000
rate = 0.0325
total = principal
years = 0

while total < principal * 2:
    total += total * rate
    years += 1

print(f"需要{years}年，本金和利息才能翻倍。")
