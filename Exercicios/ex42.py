# Variavel de input
numero_str = input(
    "Vou dobrar o numero que voce digitar aqui: "
)

if numero_str.isdigit():
    numero_float = float(numero_str)
    print(f'O dobro de {numero_float:.1f} é {numero_float * 2:.1f}')
else:
    print('Voce digitou um valor não numerico')