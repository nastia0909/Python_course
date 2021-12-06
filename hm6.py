model = input('type model of the car ')
while True:
    if model in ['mondeo', 'focus', 'kuga']:
        print("ford")
    elif model in ['tipo', 'panda', '500']:
        print("fiat")
    elif model in ['clio', 'megan', 'duster']:
        print("renault")
    else:
        print('Wrong model')
    model = input('type model of the car ')
    if model == 'exit':
        break






