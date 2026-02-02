"""实现一个简单的ToDo List（待办事项列表）功能，实现添加，删除，置顶和完成的代办事项
todo_list = []
while True:
    print("========== ToDo List ==========")
    print("1. 添加代办事项")
    print("2. 删除代办事项")
    print("3. 置顶代办事项")
    print("4. 完成代办事项")
    print("5. 退出")

========== 当前代办事项 ==========
1. learn Python         [未完成]
2. learn C++            [已完成]
3. learn database       [未完成]"""

todo_list = []

while True:
    print("========== ToDo List ==========")
    print("1. 添加代办事项")
    print("2. 删除代办事项")
    print("3. 置顶代办事项")
    print("4. 完成代办事项")
    print("5. 退出")
    
    choice = input("请选择操作（1-5）：")
    
    if choice == '1':
        item = input("请输入代办事项内容：")
        todo_list.append({'task': item, 'status': '未完成'})
        print(f"已添加代办事项: {item}")
    
    elif choice == '2':
        for idx, todo in enumerate(todo_list, 1):
            print(f"{idx}. {todo['task']} [{todo['status']}]")
        del_index = int(input("请输入要删除的代办事项编号：")) - 1
        if 0 <= del_index < len(todo_list):
            removed_item = todo_list.pop(del_index)
            print(f"已删除代办事项: {removed_item['task']}")
        else:
            print("无效的编号！")
    
    elif choice == '3':
        for idx, todo in enumerate(todo_list, 1):
            print(f"{idx}. {todo['task']} [{todo['status']}]")
        top_index = int(input("请输入要置顶的代办事项编号：")) - 1
        if 0 <= top_index < len(todo_list):
            item_to_top = todo_list.pop(top_index)
            todo_list.insert(0, item_to_top)
            print(f"已置顶代办事项: {item_to_top['task']}")
        else:
            print("无效的编号！")
    
    elif choice == '4':
        for idx, todo in enumerate(todo_list, 1):
            print(f"{idx}. {todo['task']} [{todo['status']}]")
        complete_index = int(input("请输入要完成的代办事项编号：")) - 1
        if 0 <= complete_index < len(todo_list):
            todo_list[complete_index]['status'] = '已完成'
            print(f"已完成代办事项: {todo_list[complete_index]['task']}")
        else:
            print("无效的编号！")
    
    elif choice == '5':
        print("退出程序。")
        break
    
    else:
        print("无效的选择，请重新输入！")
