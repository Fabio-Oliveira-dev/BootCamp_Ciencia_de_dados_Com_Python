# 1 - 2012 o campeão, Joey Chestnut, devorou 68 cachorros-quentes em dez minutos
# um aumento incrível em relação aos 62 sanduíches devorados pelo mesmo Chestnut em 2011.

# 2 - informar o número médio de cachorros-quentes consumidos pelos participantes durante a competição.

# 3 - A entrada consiste de uma única linha que contém dois inteiros H e P (1 ≤ H, P ≤ 1000) 
# indicando respectivamente o número total de cachorros-quentes consumidos e o número total de participantes na competição.


valores = input().split()

cachorros_quentes = int(valores[0])
pessoas = int(valores[1])

media_cachorros_quentes = cachorros_quentes / pessoas

media_cachorros_quentes_float = f"{media_cachorros_quentes:.2f}"

print(media_cachorros_quentes_float)