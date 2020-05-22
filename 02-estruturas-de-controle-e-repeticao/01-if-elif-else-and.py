
idade = int(input('Qual sua idade?'))

# 1) if
if idade < 18:
    print('Proibida a entrada de menores...')

if idade >= 18:
    print('Pode entrar!')
    bebida = input('Qual bebida você quer?')
    print('Segue sua bebida {}'.format(bebida))

# 2) if else
if idade < 18:
    print('Proibida a entrada de menores...')

else:
    print('Pode entrar!')
    bebida = input('Qual bebida você quer?')
    print('Segue sua bebida {}'.format(bebida))

# 3) elif

if idade < 18:
    print('Proibida a entrada de menores...')

elif idade >= 18 and idade < 21: # or
    print('Pode entrar! Mas só bebe água e leite!')

else:
    print('Pode entrar!')
    bebida = input('Qual bebida você quer?')
    print('Segue sua bebida {}'.format(bebida))