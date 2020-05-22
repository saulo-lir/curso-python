# Atribuição múltipla

x, y, z = 10, 20, 30
print('{} {} {}'.format(x, y, z))

x = y = z = 10

w = 10
w += 20
w -= 10
w *= 2
w /= 3

print(w)

# Operadores condicionais

nota = 8

if nota >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'

print(situacao)

# if reduzido

situacao = 'Aprovado' if nota >= 7 else 'Reprovado'
print(situacao)