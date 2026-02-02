""" 基于以下数据结构实现一个购物车系统，可以添加商品到购物车，删除商品，打印当前购物车所有商品以及总价。
	shopping_cart = [
		{
			'name': 'mac电脑',
			'price': 14999,
			'quantity': 1
		},
		{
			'name': 'iphone15',
			'price': 9980,
			'quantity': 1 
		}
	] """

shopping_cart = [
    {
		'name': 'mac电脑',
		'price': 14999,
		'quantity': 1
	},
    {
		'name': 'iphone15',
		'price': 9980,
		'quantity': 1
	}
]

def add_item(name, price, quantity):
	shopping_cart.append({
		'name': name,
		'price': price,
		'quantity': quantity
	})

def remove_item(name):
	global shopping_cart
	shopping_cart = [item for item in shopping_cart if item['name'] != name]

def print_cart():
	total_price = 0
	print("购物车内容:")
	for item in shopping_cart:
		item_total = item['price'] * item['quantity']
		total_price += item_total
		print(f"商品: {item['name']}, 价格: {item['price']}, 数量: {item['quantity']}, 总计: {item_total}")
	print(f"总价: {total_price}")

def main():
	print(shopping_cart)
	print('------进行购物车操作------')
	print('1.添加商品\n2.删除商品\n3.打印购物车内容\n')
	choice = input("请选择操作 (1/2/3): ")
	if choice == '1':
		name = input("请输入商品名称: ")
		price = int(input("请输入商品价格: "))
		quantity = int(input("请输入商品数量: "))
		add_item(name, price, quantity)
	elif choice == '2':
		name = input("请输入要删除的商品名称: ")
		remove_item(name)
	elif choice == '3':
		print_cart()
	else:
		print("无效选择，请重新输入。")

if __name__ == "__main__":
	main()
