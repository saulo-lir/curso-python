# Definindo uma função

def exibir_nome():
    print('Curso de Python')

def somar(num1, num2):
    return num1 + num2

exibir_nome()

x = 5
y = 10

print('{} + {} = {}'.format(x, y, somar(x,y)))