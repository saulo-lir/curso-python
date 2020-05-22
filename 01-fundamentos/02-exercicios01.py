'''
Exercício 1
---
Um script que leia o nome de uma pessoa, depois exiba na tela uma mensagem
de boas-vindas, com o nome da pessoa digitado.

Exercício 2
---
Receba o dia, o mês e o ano de nascimento de uma pessoa.
Exiba a data formatada.

Exercício 3
---
Crie um script que leia 2 números e mostre a soma deles.
'''

# Exercício 1

nome = input('Quem é você?\n')
print('\nBem vindo(a): '+nome)

# Exercício 2

dia = input('Dia de nascimento:\n')
mes = input('Mês:\n')
ano = input('Ano:\n')

#print('Você nasceu em:', dia, '/', mes, '/', ano)

# Exercício 3

n1 = input('Número 1: ')
n2 = input('Número 2: ')

print('A soma é:', int(n1) + int(n2))

# Converter o tipo de entrada:

n1 = int(input('Número 1: '))
n2 = int(input('Número 2: '))

print('A soma é:', n1+n2)