# 初始化客户信息列表
customers = { 
	"1001":{
		"name":"Alice",
		"age":25,
		"email":"alice@example.com"
	},
	"1002":{
		"name":"Bob",
		"age":28,
		"email":"bob@example.com"
	}
}

while True:
    print("*" * 25)
    print("""
        1. 添加客户信息
        2. 删除客户信息
        3. 修改客户信息
        4. 查询某位客户信息
        5. 查询所有客户信息
        6. 退出系统
    """)
    print("*" * 25)

    choice = input("请输入您的选择：")

    #（1）添加客户
    if choice == "1":
        ID = input("请输入添加客户的ID：")
		
        if ID in customers:
            print("该ID已存在！")
        else:
            name = input("请输入添加客户的姓名：")
            age = input("请输入添加客户的年龄：")
            email = input("请输入添加客户的邮箱：")
            new_customer = {
				"name":name,
				"age":age,
				"email":email
			}

            customers.update({ID:new_customer})
            print(f"添加客户 {name} 成功！")
    #（2）删除客户（默认姓名不重复）
    elif choice == "2":
        del_customer_ID = input("请输入删除客户的ID：")
        if del_customer_ID in customers:
            customers.pop(del_customer_ID)
            print(f"已删除 {del_customer_ID} 客户信息！")
        else:
            print("该ID不存在！")
    #（3）修改客户
    elif choice == "3":
        update_customer_ID = input("请输入你想要修改的客户的ID：")
        if update_customer_ID in customers:
            new_name = input("请输入修改后的客户的姓名：")
            new_age = input("请输入修改后客户的年龄：")
            new_email = input("请输入修改后的客户的邮箱：")

            customers[update_customer_ID].update({"name":new_name, "age":new_age, "email":new_email})
            print(f"{update_customer_ID} 客户信息已修改！")
            print("最新信息如下！\n", customers)
        else:
            print(f"未找到 {update_customer_ID} 信息！")
    #（4）查看某一个客户
    elif choice == "4":
        query_customers_ID = input("请输入要查看的客户的ID：")
        if query_customers_ID in customers:
            customer_ID = customers[query_customers_ID]
            print(f"姓名：{customer_ID.get('name'):^10}, 年龄：{customer_ID.get('age'):^3}, 邮箱：{customer_ID.get('email'):^25}")
        else:
            print("该客户 {ID} 不存在！")
    #（5）查看每一位客户的信息
    elif choice == "5":
        if customers:
            for key, customer_meg in customers.items():
                print(f"客户ID：{key:^4}, 姓名：{customer_meg.get('name'):^10}, 年龄：{customer_meg.get('age')^3}, 邮箱：{customer_meg.get('email'):^25}")
        else:
            print("当前没有任何客户信息！")
    #（6）退出系统
    elif choice == "6":
        print("已退出程序！")
        exit()

    else:
        print("输入的内容无效，请重新输入！")
