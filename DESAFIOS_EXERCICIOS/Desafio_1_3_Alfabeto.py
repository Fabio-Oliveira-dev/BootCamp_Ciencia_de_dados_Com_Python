
lista_letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 
'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
    'T', 'U', 'V', 'W', 'X', 'Y', 'Z',]

entrada_letra = str(input()).upper()
pos = lista_letras.index(entrada_letra)
print(pos + 1)
