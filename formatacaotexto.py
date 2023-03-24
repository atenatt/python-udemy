""" Exercicio Aula 31 """

nome = str('Victor Pedro')
altura = float(1.80)
peso = int(95)
imc = (peso / (altura * altura)) # IMC = peso / (altura x altura)
# imc = peso / altura ** 2 # IMC = peso / (altura x altura)

# f - string
linhas_1 = f'{nome} tem {altura} de altura'
linhas_2 = f'pesa {peso} quilo e seu IMC é'
linhas_3 = f'{imc:.2f}'
print(linhas_1)
print(linhas_2)
print(linhas_3)

# Casas decimais
# decimais = f'{nome} tem {altura:.2f} de altura'
# print (decimais)

# Texto puro
# print(nome, "tem", altura, "de altura,")
# print("pesa", peso, "quilos e seu IMC é")
# print (imc)