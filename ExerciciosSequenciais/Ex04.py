# Questão 4. Faça um Programa que peça as 4 notas bimestrais e mostre a média.

num1 = float(input('Digite a 1° nota: '))
num2 = float(input('Digite a 2° nota: '))
num3 = float(input('Digite a 3° nota: '))
num4 = float(input('Digite a 4° nota: '))
media = (num1 + num2 + num3 + num4)/4
print(f'A media das notas é: {media:.2f}')