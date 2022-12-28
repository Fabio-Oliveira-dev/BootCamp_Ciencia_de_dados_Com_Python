print('=' * 20)
print('{:^20}'.format('Banco FB'))
print('=' * 20)
print('Escolha abaixo a operação que deseja realizar!')
menu = """
[ 1 ] Depositar
[ 2 ] Sacar
[ 3 ] Extrato
[ 0 ] Sair

=> """

saldo = 0
limite = 500
extrato = ''
numero_saques = 0
LIMITE_SAQUE = 3

while True:
    opcao = input(menu)

    if opcao == '1':
        print('Depositar')
        valor = float(input('Digite o valor do deposito: '))

        if valor > 0:
            saldo += valor
            extrato += f'Deposito de \033[0;34mR$ {valor:.2f}\033[m reais realizado com sucesso.\n'

        else:
            print('Operação falhou! O valor informado é invalido.')

    elif opcao == '2':
        print('Sacar')
        valor = float(input('Qual o valor que você deseja sacar? '))
        
        excedeu_saldo = valor > saldo # Verificar se excedeu o saldo

        excedeu_limite = valor > limite # Verificar se excedeu o limite

        excedeu_saques = numero_saques >= LIMITE_SAQUE # verificar se já fez os 3 saques

        if excedeu_saldo:
            print('Operação falhou! Você não tem saldo suficiente.')

        elif excedeu_limite:
            print('Operação falhou! O valor do saque excede o limite.')
        
        elif excedeu_saques:
            print('Operação falhou! Número máximo de saques diários excedido.')

        elif valor > 0:
            saldo -= valor
            extrato += f'Saque: \033[0;31mR$ {valor:.2f}\033[m reais\n'
            numero_saques += 1

        else:
            print('Operação falhou! O valor informado é inválido.')

    elif opcao == '3':
        print('='*20, 'Extrato', '='*20)
        print('Não foram realizada movimentações' if not extrato else extrato)
        print(f'\nSeu Saldo atual é de: \33[0;34mR$ {saldo:.2f}\033[m reais.')
        print('='*49)

    elif opcao == '0':
        break

    else:
        print('Operação inválida, selecione novamente a operação que deseja realizar')
    
