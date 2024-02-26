# 2. Mostrar a média aritmética entre 3 números fornecidos pelo usuário.
number1 = int(input('Digite um número: '))
number2 = int(input('Digite outro número: '))
number3 = int(input('Digite o terceiro número: '))

average = (number1 + number2 + number3)/3

print('A média dos valores digitados é:', f'{average:.2f}')