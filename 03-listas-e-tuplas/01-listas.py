# 1) Inicializando uma lista

lista1 = list()

lista2 = []

lista3 = [1, 89, 6.8, 0, 'food']
print(lista3)

lista4 = list(('Python'))
print(lista4)

# 2) Funções da classe list

# Concatenar / Merger duas ou mais listas

lista5 = lista3 + lista4
print(lista5)

# Adicionar um item no final da lista

numeros = [1,2,4,5]
print(numeros)

numeros.append(99)
print(numeros)

# Remover um item da lista

del(numeros[1])
print(numeros)

# Adicionar um item numa posição específica da lista

numeros.insert(1, 20) # Na posição 1, insira 20

# Limpar a lista

numeros.clear()

# 3) Iterar sobre a lista

lista1 = [2,0,6,7,94]

# # Ex1:
for item in lista1:
    print(item)

# #Ex2:
i = 0
count = len(lista1)

while i < count:
    print(lista1[i])
    i += 1

# #Ex3:
for idx in range(len(lista1)):
    lista1[idx] += lista1[idx] + 50

print(lista1)

#Ex4:
# O enumerate devolve o índice e o valor da lista. O índice é gravado na variável idx, e o valor na variável item
for idx, item in enumerate(lista1):
    print('Índice: {}'.format(idx))
    print('Valor: {}'.format(item))


# 4) Fatiando uma lista

print(lista1[1:3])