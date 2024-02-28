# Questão 12. Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um
# algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas: Para homens: (72.7*h) – 58
# Para mulheres: (62.1*h) - 44.7 (h = altura) Peça o peso da pessoa e informe se ela está dentro,
# acima ou abaixo do peso.

sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = input('Digite seu sexo [M/F]: ').upper()

altura = float(input('Digite sua altura(m): '))
peso = float(input('Digite seu peso(kg): '))

if sexo == 'M':
    idealHomem = (72.7 * altura) - 58
    print(f'Seu peso ideal é de {idealHomem:.2f}kg')
    if round(peso) < round(idealHomem):
        print(f'Seu peso está abaixo do ideal')
    elif round(peso) > round(idealHomem):
        print(f'Seu peso está acima do ideal')
    else:
        print(f'Seu peso está no peso ideal')
elif sexo == 'F':
    idealMulher = (62.1 * altura) - 44.7
    print(f'Seu peso ideal é de {idealMulher:.2f}kg')
    if round(peso) < round(idealMulher):
        print(f'Seu peso está abaixo do ideal')
    elif round(peso) > round(idealMulher):
        print(f'Seu peso está acima do ideal')
    else:
        print(f'Seu peso está no peso ideal')
else:
    print('Sexo invalido')
