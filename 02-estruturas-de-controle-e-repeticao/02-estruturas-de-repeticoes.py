# 1) for

for n in range(1, 10): # Intervalo de 1 a 9
    print(n)

for i in range(5): # Intervalo de 0 a 5
    print(i)


tabuada = 6

for num in range(1,11):
    print('{} x {} = {}'.format(num, tabuada, num * tabuada))


inicio = int(input('Início: '))
final = int(input('Final: '))
intervalo = int(input('Intervalo: '))

# O terceiro parâmetro é quantidade de vezes que será pulado a exibição do valor dentro do loop
for num in range(inicio, final, intervalo):
    print('Número {}'.format(num))


# Usando o break
for num in range(0,6):
    print(num)

    if num == 2:
        break   # Quebrando o loop

print('Final')

# Usando o continue
for num in range(0,6):
    print(num)

    if num == 2:
        continue   # O continue faz o loop voltar pro início. Então quando num == 2, o print('Final') não será executado, pois o loop vai continuar do início.
    print('Final')


# 2) while

num1 = 1
num2 = 0
soma = num1 + num2

while soma > 0:
    num1 = int(input('Número 1: '))
    num2 = int(input('Número 2: '))
    soma = num1 + num2
    print('{} + {} = {}'.format(num1, num2, soma))