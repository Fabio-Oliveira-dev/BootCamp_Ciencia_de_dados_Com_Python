'''
1 - A entrada é composta por 3 inteiros, que indicam, respectivamente, a distância entre os Palantír,
o diâmetro do Palantír de Sauron e o diâmetro do Palantír de Saruman.

2 - A saída é um valor real indicando o ICM da comunicação dos Palatír de Sauron e Saruman, com 2 casas decimais.

3 - para calcular o ICM para Palantír’s, basta dividir a distância entre os dois Palantír’s, pela soma do diâmetro dos mesmos.
'''

# Usei o map para aplicar a função para todos os itens da lista
# O usuario digita 3 valores de classe int referente às medicas atráves do input
# O metodo split para fazer a separação de strings
distancia, diametro1, diametro2 = map(int, input('Digite os valores de distância, diametro1, diametro2: ').split(" "))

# Resultado com 2 casas decimais
print(f"{(distancia / (diametro1 + diametro2)):.2f}")
