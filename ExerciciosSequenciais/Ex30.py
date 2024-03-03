# Questão 30. Elabore um algoritmo que lê um número, mostra a metade e a terça parte deste número.
numero = float(input('Digite um número: '))
metade = numero / 2
terco = numero / 3
print(f'Número: {numero}')
print(f'Metade: {metade}')
print(f'Terço: {terco:.2f}')