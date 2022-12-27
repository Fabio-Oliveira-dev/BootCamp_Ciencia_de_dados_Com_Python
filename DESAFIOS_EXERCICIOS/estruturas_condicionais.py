MAIOR_IDADE = 18
IDADE_ESPECIAL = 17
idade = int(input('Informe a sua idade: '))
'''if idade >= MAIOR_IDADE:
    print('Você é maior de idade, ja pode tirar a CNH.')
if idade <= MAIOR_IDADE:
    print('Você é menor de idade e ainda não pode tirar a CNH.')'''


'''if idade >= MAIOR_IDADE:
    print('Você é maior de idade, ja pode tirar a CNH')
else:
    print('Você é menor de idade e ainda não pode tirar a CNH.')'''

if idade >= MAIOR_IDADE:
    print('Você é maior de idade, ja pode tirar a CNH')
elif idade == IDADE_ESPECIAL:
    print('Você pode fazer apenas as aulas teoricas e não as aulas praticas.')
else:
    print('Você é menor de idade e ainda não pode tirar a CNH.')
