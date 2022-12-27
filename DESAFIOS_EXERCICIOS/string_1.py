'''nome = 'FaBIo'


print(nome.upper()) # metodo que deixa tudo em maiusculo
print(nome.lower()) # Tudo em inusculo
print(nome.title()) # Só a primeira letra em maiusculo


texto = '  Olá mundo!      '
print(texto + '.') # Com os espeços
print(texto.strip() + '.') # Remove os espaços dos dois lados
print(texto.lstrip() + '.') # Remove os espaços da esquerda
print(texto.rstrip() + '.') # Remove os espaços da direita'''


nome = 'Java'
print('####' + nome + '####')
print(nome.center(14)) # Dividir o texto em espeços exatamente iguais
print(nome.center(14, '#')) # Dividir do jeito certo sem ficar calculando na mão
print('J_a_v_a')
print('_'.join(nome)) # Colocar caracteres entre as caracteres da string
