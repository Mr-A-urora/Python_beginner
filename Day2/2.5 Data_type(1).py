from decimal import Decimal

# 整形
a = 1
b = 2
print(a + b)

# 浮点型
x = 1.78
y = 4.97
print(x + y)
print(x - y)

# 精度限制的方法：
"""方法一：四舍五入
ret = round(x - y, 2)
print(ret)"""

# 方法二：调用函数处理数据
"""x = Decimal("1.78")
y = Decimal("4.97")
print(x - y)"""

# type() 打印数据对象类型名
print(type(a))
print(type(x))