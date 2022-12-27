nome = 'Fábio Oliveira'
idade = 29
profissão = 'programador'
linguagem = 'python'
saldo = 45.435
dados = {'nome': 'Fabio Oliveira', 'idade': '29'} # Dicionário


# Interpolação 1 usando %
print('Nome: %s Idade: %d' % (nome, idade))

# Interpolação 2 usando o .format
print('Nome: {} Idade: {}'.format(nome, idade))

# Interpolação 2 usando o .format, porem agora informando os indices dentro de chaves {}
print('Nome: {0} Idade: {1}'.format(nome, idade))

# Nesse exemplo eu posso passar o indice varias vezes, ou seja, reaproveitar as variáveis
print('Nome: {0} Idade: {1} {0} {0}'.format(nome, idade))

# Outra forma de usar o .format é passar os indices nomeados
print('Nome: {nome} Idade: {idade}'.format(nome=nome, idade=idade))

# Passar as informações usando o dicionário criado
print('Nome: {nome} Idade: {idade}'.format(**dados))

# Interpolação 3 usando o f string
print(f'Nome: {nome} Idade: {idade} Saldo: {saldo:10.2f}')

print(f'Nome: {nome} Idade: {idade} Saldo: {saldo:.2f}')
print(f'{nome} {idade} {saldo:.2f}')