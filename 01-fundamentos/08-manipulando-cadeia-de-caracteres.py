# 1) Fatiamento

frase = 'You Shall Not Pass!!!'
print(frase[2]) # Imprimir uma posição específica da string
print(frase[2:8]) # Imprimir um intervalo de caracteres
print(frase[3:10:2]) # Comece na posição 3 e vá até a 10, exibindo de 2 em 2
print(frase[:5]) # Exibir os 5 primeiros caracteres
print(frase[5:]) # Imprime a partir do 5 caractere

# 2) Análise

print(len(frase)) # Imprimir tamanho da string
print(frase.count('s')) # Contar quantas vezes aparece a letra 's'
print(frase.find('Pass')) # Procurar em que posição um caractere/string começa
print('You' in frase) # Verifica se um caractere/string existe

# 3) Transformação

print(frase.replace('You', 'Você')) # Trocar uma string por outra
print(frase.upper()) # Converter minúsculas em maiúsculas
print(frase.lower()) # Converter maiúsculas em minúsculas
print(frase.capitalize()) # Converter apenas a primeira letra em maiúscula
print(frase.title()) # Converter as primeiras letras de cada palavra em maiúsculas

frase2 = '     You Shall Not Pass      '

print(frase.strip()) # Remove os espaços em branco do início e do final da string

# 3) Divisão

print(frase.split()) # ['You', 'Shall', 'Not', 'Pass!!!']

# 4) Junção

frase3 = ['Um', 'Dois', 'Três']
print(', '.join(frase3))