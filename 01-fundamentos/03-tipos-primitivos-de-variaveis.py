# Imprimir o tipo da variável

n1 = int(input('Número 1:'))
print(type(n1))

n2 = float(input('Número 2:'))
print(type(n2))

soma = n1 + n2

print('A soma de {} e {} vale {}'.format(n1, n2, soma))

boleano = bool(input('Número:')) # Se digitar qualquer valor, então o resultado será True, senão será False
print(boleano)

# Verificar se o valor é de determinado tipo

nome = input('Nome: ')
print(nome.isnumeric())