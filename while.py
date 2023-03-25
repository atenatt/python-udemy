"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
Loop infinito -> Quando um código não tem fim
"""
CONDICAO = True

while CONDICAO:
    print("Digite 'Sair' para sair do programa")
    nome = input("Digite seu nome: ")
    print(f'Seu nome é: {nome}')
    
    if nome == 'Sair':
        break