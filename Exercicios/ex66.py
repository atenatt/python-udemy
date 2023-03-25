""" Calculadora com while """

while True:
    numero_1 = input('Digite um numero: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')
    
    numero_1.isdigit():
    
    if operador == '+':
        resultado = numero_1_float + numero_2_float
        print(f'O resultado da sua conta é: {numero_1_float} + {numero_2_float} = {resultado}')
    elif operador == '-':
        resultado = numero_1_float - numero_2_float
        print(f'O resultado da sua conta é: {numero_1_float} - {numero_2_float} = {resultado}')
    elif operador == '/':
        resultado = numero_1_float / numero_2_float
        print(f'O resultado da sua conta é: {numero_1_float} / {numero_2_float} = {resultado}')
    elif operador == '*':
        resultado = numero_1_float * numero_2_float
        print(f'O resultado da sua conta é: {numero_1_float} * {numero_2_float} = {resultado}')
    else:
        print("Algo de errado aconteceu...")

    sair = input('Deseja sair? [s]im: ').lower().startswith('s')
    
    if sair is True:
        break