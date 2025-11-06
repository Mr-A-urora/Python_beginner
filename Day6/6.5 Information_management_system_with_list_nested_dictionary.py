# 初始化客户信息列表
customers = [ 
	{
		"name":"Alice",
		"age":25,
		"email":"alice@example.com"
	}, {
		"name":"Bob",
		"age":28,
		"email":"bob@example.com"
	}
]

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

    #（1）添加客户 append
    if choice == "1":
        name = input("请输入添加客户的姓名：")
        age = input("请输入添加客户的年龄：")
        email = input("请输入添加客户的邮箱：")
        new_customer = {
			"name":name,
			"age":age,
			"email":email
        }
        customers.append(new_customer)
        print(f"添加客户 {name} 成功！")
    #（2）删除客户（默认姓名不重复）
    elif choice == "2":
        del_customer_name = input("请输入删除客户的姓名：")
        flag = False
        for customer_dict in customers:
            if customer_dict.get("name") == del_customer_name:
                customers.remove(customer_dict)
                print(f"{del_customer_name} 删除成功！")
                flag = True
                break

        if flag:
            print("信息已更新！\n", customers)
        else:
            print(f"未找到 {del_customer_name}")
    #（3）修改客户
    elif choice == "3":
        update_customer_name = input("请输入你想要修改的客户的姓名：")
        flag = False

        for customer_dict in customers:
            if customer_dict.get("name") == update_customer_name:
                new_name = input("请输入修改后的客户的姓名：")
                new_age = input("请输入修改后客户的年龄：")
                new_email = input("请输入修改后的客户的邮箱：")
                customer_dict.update({"name":new_name, "age":new_age, "email":new_email})
                print(f"{update_customer_name} 客户信息已修改！")
                flag = True
                break

        if flag:
            print("最新信息如下！\n", customers)
        else:
            print(f"未找到 {update_customer_name} 信息！")
    #（4）查看某一个客户
    elif choice == "4":
        query_customers_name = input("请输入要查看的客户的姓名：")
        flag = False

        for customer_dict in customers:
            if customer_dict.get("name") == query_customers_name:
                print(f"姓名：{customer_dict.get('name'):^10}, 年龄：{customer_dict.get('age'):^3}, 邮箱：{customer_dict.get('email'):^25}")
                flag = True
                break

        if not flag:
            print(f"未查询到 {query_customers_name} 的相关信息！")
    #（5）查看每一位客户的信息
    elif choice == "5":
        if customers:
            for customer_dict in customers:
                print(f"姓名：{customer_dict.get('name'):^10}, 年龄：{customer_dict.get('age'):^3}, 邮箱：{customer_dict.get('email'):^25}")
        else:
            print("当前没有任何客户信息！")
    #（6）退出系统
    elif choice == "6":
        print("已退出程序！")
        exit()

    else:
        print("输入的内容无效，请重新输入！")
