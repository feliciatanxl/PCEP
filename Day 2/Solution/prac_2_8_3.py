my_list = []

while True:
    num = int(input("Enter a number: "))
    if num == 0:
        break
    
    for i in range(len(my_list)):
        if num <= my_list[i]:
            my_list.insert(i, num)
            break

        if i == len(my_list) - 1:
            my_list.append(num)
    
    if len(my_list) == 0:
        my_list.append(num)

    print(my_list)