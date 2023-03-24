""" Exercicio 38 """

# Variaveis #
primeiro_valor = input('Digite um valor: ')
segundo_valor = input('Digite o segundo valor: ')

# Declarando variaveis como inteiro #
int_primeiro_valor = int(primeiro_valor)
int_segundo_valor = int(segundo_valor)


# CODIGO #
if int_primeiro_valor > int_segundo_valor:
    print(
        f'{int_primeiro_valor=} é maior que {int_segundo_valor=}'
        )
    
elif int_primeiro_valor < int_segundo_valor:
    print(
        f'{int_segundo_valor=} é maior que {int_primeiro_valor=}'
        )
    
elif int_primeiro_valor == int_segundo_valor:
    print(
        f'{int_primeiro_valor=} é igual ao {int_segundo_valor=}'
        )
    
else:
    print(
        'Error: voce digitou algo errado.'
        )