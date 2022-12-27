# AND = para ser True tudo tem que ser True.
# OR = para ser True apenas um tem que ser True.

#verdadeiro
print(True and True)
#Falso
print(True and False)
#Falso
print(False and False)
#Verdadeiro
print(True or True)
#Verdadeiro
print(True or False)
#Falso
print(False or False)

saldo = 1000
saque = 250
limite = 200
conta_especial = True


expressao = saldo >= saque and saque <= limite or conta_especial and saldo >= saque
print(expressao)

expressao_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saque)
print(expressao_2)

conta_normal_com_saldo_suficiente = saldo >= saque and saque >= limite
conta_especial_com_saldo_suficiente = conta_especial and saldo >= saque

expressao_3 = conta_normal_com_saldo_suficiente or conta_especial_com_saldo_suficiente
print(expressao_3)
