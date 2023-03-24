# Operadores lógicos
# and (e) or (ou) not (não)
# and - Todas as condições precisam ser
# verdadeiras.
# Se qualquer valor for considerado falso,
# a expressão inteira será avaliada naquele valor
# São considerados falsy (que vc já viu)
# 0 0.0 '' False
# Também existe o tipo None que é
# usado para representar um não valor

print('[E]ntrar [S]air: ')
entrada = input("")

if entrada == 'E' or entrada == 'e':
    senha = input("Digite a senha: ")
    if senha == "123":
        print("Entrada liberada")
    else:
        print("Acesso negado!")
elif entrada == 'S' or entrada == 's':
    print ('Saindo do programa')
else:
    print("Voce nao digitou [E] nem [S]")
    print("Saindo do programa...")
