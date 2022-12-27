valores = input().split()

cachorros_quentes = int(valores[0])
pessoas = int(valores[1])

media_cachorros_quentes = cachorros_quentes / pessoas

media_cachorros_quentes_float = f"{media_cachorros_quentes:.2f}"

print(media_cachorros_quentes_float)