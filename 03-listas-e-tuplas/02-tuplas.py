'''
As tuplas não permitem serem alteradas. São listas imutáveis.
Geralemnte são utilizadas para guardar elementos distintos

'''
# A inicialização é com parênteses
data = ('11', 'Domingo', 'Fevereiro', 2020)
print(data)
print(data[3])

# A inicialização também pode ser sem parênteses (As vírgulas nesse caso é que definem a tupla)
data = 1,2,3
print(data)
print(type(data))

# Também podemos utilizar a classe tuple
data = tuple('Python')