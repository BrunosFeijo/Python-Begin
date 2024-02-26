# 13. Leia o numerador e o denominador de uma fração e transforme-o em um número decimal.
numerador = float(input("Digite o numerador da fração: "))
denominador = float(input("Digite o denominador da fração: "))

numero_decimal = numerador / denominador

print("O número decimal correspondente à fração é:", f'{numero_decimal:.2f}')
