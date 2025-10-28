while True:
    user_input = input("Enter a number: ")

    if user_input == "exit":
        break

    number = int(user_input)
    square = number ** 2
    print(f"{number}的平方是{square}")
