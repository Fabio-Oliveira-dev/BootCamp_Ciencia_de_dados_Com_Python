texto = input('Informe um texto: ')
VOGAIS = 'AEIOU'

# Exemplo utilizando um iteravel
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end='')
else:
    print() # Adiciona uma quebra de linha
    print('Executado com sucesso!')

# Exemplo utilizando o built-in range
for numero in range(0, 51, 5): # range(Start, stop, step)
    print(numero, end=' ')
