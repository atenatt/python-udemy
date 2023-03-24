# Operadores in e not in
# Strings são iteráveis
#  0 1 2 3 4 5
#  O t á v i o
# -6-5-4-3-2-1
# nome = 'Victor'
# # print(nome[3]) # t
# # print(nome[-3]) # t
# print('Vic' in nome)
# # print('zero' in nome)
# print(10 * '-')
# print('Vic' not in nome)
# # print('zero' not in nome)

nome = input('Digite seu nome: ')
encontrar = input('Digite o que deseja encontrar: ')

if encontrar in nome:
    print(f'{encontrar} está em {nome}')
else:
    print(f'{encontrar} não está em {nome}')