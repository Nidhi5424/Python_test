def square_list():

    list = []
    new_list = []

    for i in range(4):
        num = int(input("Enter the number to find squar of it: "))

        list.append(num)

    print(f"\nList of given number: {list}")
        
    for x in list:
        new_list.append(x ** 2)

    print(f"List of Squar of each numbers: {new_list}")


square_list()