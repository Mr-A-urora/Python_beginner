# 实现一个购物车清单，可以引导用户添加商品和删除商品

shopping_cart = []

while True:
	print("--- 购物车清单 ---")
	print("1. 添加商品")
	print("2. 删除商品")
	print("3. 查看购物车")
	print("4. 结束程序")
	
	choice = input("请输入你的选择：")
	if choice == "1":
		add_item = input("请输入要添加的商品名称：")
		shopping_cart.append(add_item)
		print(f"已添加商品：{add_item}\n\n")
	elif choice == "2":
		del_item = input("请输入删除商品的名称：")
		if (del_item in shopping_cart):
			shopping_cart.remove(del_item)
			print(f"已删除商品：{del_item}\n\n")
		else:
			print("该商品不存在此购物车中！")
			print("\n\n")
	elif choice == "3":
		if len(shopping_cart) == 0:
			print("购物车为空！")
		else:
			print("*" * 20)
			for i in shopping_cart:
				print(i)
			print("*" * 20)
		print("\n\n")
	else:
		exit() 
