num1 = input('num1: ')
action = input('operator: ')
num2 = input('num2: ')
if num1.isdigit and num2.isdigit:
    num1 = int(num1)
    num2 = int(num2)
while True:
    if action in ['+', '-', '*', '/']:
        if action == '+':
            num1 = num1 + num2
        elif action == '-':
            num1 = num1 - num2
        elif action == '/':
            num1 = num1 / num2
        elif action == '*':
            num1 = num1 * num2
    else:
        print('Error')
    action = input('operator: ')
    num2 = input('num2: ')
    if action == 'exit' or num2 == 'exit' or not num2.isdigit:
        break
    num2 = int(num2)
print(num1)










