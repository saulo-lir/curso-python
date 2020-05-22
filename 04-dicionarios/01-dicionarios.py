'''
Dicionários são estruturas representadas por chave:valor
'''
# Inicializando um dicionário
dic1 = {}

dic2 = dict()

dic3 = {'nome':'Bruna', 'idade':20, 'peso':50.5}

print('Nome {}'.format(dic3['nome']))
print('Idade {}'.format(dic3['idade']))
print('Peso {:.2f}'.format(dic3['peso']))

# As chaves também podem ser números
dic1 = {10:'Bruna', 20:'Ana', 30:50.5}
print(dic1)

# As chaves também podem ser múltiplas, usando-se uma tupla
dic2 = {(10,20):'Bruna', (30,40):'Julia'}
print(dic2[(10,20)])
print(dic2[(30,40)])

# Pegar um valor de um índice específico
dic = dict(a='carro', b='moto') # Inicializando

valor = dic.get('a')
print(valor)

# Copiar os valores de um dicionário
dic2 = dic.copy()
print(dic2)

# Verificar se algum valor existe ou não no dicionário
pessoas = {'Ana':987654321, 'Bruna': 233215487, 'Julia':645231987}
nome = input('Digite seu nome: ')

if nome in pessoas:
    print('Telefone: {}'.format(pessoas[nome]))

if nome not in pessoas:
    print('O nome informado não existe na nossa base de dados')

# Concatenar / Merger 2 ou mais dicionários
pessoas2 = {'Gandalf':213423458, 'Morgoth':654321987}

pessoas.update(pessoas2)
print(pessoas)

# Iterar sobre um dicionário
for key in pessoas:
    print(key)  # Imprimir as chaves

for values in pessoas.values(): # Pegar os valores
    print(values)

for key, values in pessoas.items(): # Pegar as chaves e os valores
    print(key)
    print(values)

# Pegar apenas as chaves ou valores de um dicionário, e convertê-los para uma lista
chaves = list(pessoas.keys())
valores = list(pessoas.values())

print(chaves)
print(valores)

# Converter listas em dicionário
chaves = ['Gandalf', 'Bruna', 'Ana']
valores = [1000, 23, 28]

dicionario = dict(zip(chaves, valores))
print(dicionario)