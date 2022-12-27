def sacar(valor):
    saldo = 1000
    if saldo >= valor:
        print('Valor sacado!')
        print('Retirar o seu dinheiro da boca do caixa!')
    print('Obrigado por ser nosso cliente e tenha um bom dia!.')

def depositar(valor):
    saldo = 500
    saldo += valor

sacar(500)
