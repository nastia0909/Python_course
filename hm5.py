number = int(input('Insert the number: '))
num_list = []
for num1 in range(1, number):
    for num2 in range(2, num1):
        if num1 % num2 == 0:
            break
    else:
        num_list.append(num1)
print(num_list)







