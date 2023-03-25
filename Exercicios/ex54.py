"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""


# numero = input("Digite um número inteiro: ")

# if numero.isdigit():
#     numero = int(numero)
#     resto_numero = (numero % 2)
#     if resto_numero == 0:
#         print(f'O número {numero} é par')
#     else:
#         print(f'O número {numero} é impar')
# else:
#     print('O valor digitado nao é um número inteiro.')



"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

# hora = input("Digite a hora: ")

# if hora.isdigit():
#     hora = int(hora)
#     if hora >= 0 and hora <= 11:
#         print('Bom dia!')
#     elif hora > 11 and hora <= 17:
#         print('Boa tarde!')
#     elif hora > 17 and hora <= 23:
#         print('Boa noite!')
#     else:
#         print('Horario digitado nao esta entre 00 e 23 horas')
# else:
#     print('Valor digitado nao é um digito')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

nome = input('Digite seu primeiro nome: ')
if nome.isalpha():
    if len(nome) > 0 and len(nome) <= 4:
        print('Seu nome é curto')
    elif len(nome) > 4 and len(nome) <= 6:
        print('Seu nome é normal')
    else:
        print('Seu nome é muito grande')
else:
    print('Erro: Nome deve possuir apenas letras!')