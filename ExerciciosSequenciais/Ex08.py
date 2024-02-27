# Questão 8. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor = float(input('Digite o seu ganho por hora: $'))
hora = float(input('Digite a quantidade de horas trabalhadas neste mês: '))
salario = valor * hora
print(f'Seu salario é ${salario:.2f}')

