# 获取用户输入圆的半径，使用圆的周长和面积公式计算并打印出输入半径的圆的周长和面积
r = float(input('请输入圆的半径:'))

Perimeter = 2 * 3.1415926 * r
Area = 3.1415926 * (r ** 2)
 
print('圆的周长为:{:.2f}\n圆的面积为:{:.4f}'.format(Perimeter, Area))
