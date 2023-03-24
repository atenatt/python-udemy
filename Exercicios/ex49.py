"""
Exercício
Peça ao usuário para digitar seu nome
Peça ao usuário para digitar sua idade
Se nome e idade forem digitados:
    Exiba:
        Seu nome é {nome}
        Seu nome invertido é {nome invertido}
        Seu nome contém (ou não) espaços
        Seu nome tem {n} letras
        A primeira letra do seu nome é {letra}
        A última letra do seu nome é {letra}
Se nada for digitado em nome ou idade: 
    exiba "Desculpe, você deixou campos vazios."
"""
# Variaveis de input 
user_name = input("Digite seu nome: ")
user_age = input("Digite sua idade: ")

# Codigo 
if user_name and user_age:

    # Mostra o nome
    print(f'\nSeu nome é: {user_name}')

    # Mostra o nome invertido
    print(f'Seu nome invertido é: {user_name[::-1]}')

    # Verifica se há espaços no nome
    if (" " not in user_name):
        print(f'{user_name} não tem espaço')
    else:
        print(f'{user_name} tem espaços')
        
    # Verifica quantas letras tem seu nome
    caracteres=len(user_name)
    print(f'{user_name} tem {caracteres} caracteres')

    # Mostra a primeira letra do nome
    print(f'A primeira letra do seu nome é {user_name[0]}')

    # Mostra a ultima letra do nome
    print(f'A ultima letra do seu nome é {user_name[-1]}\n')

else:
    print(f'Desculpe, voce deixou campos vazios.')