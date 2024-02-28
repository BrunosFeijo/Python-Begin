# Questão 14. Faça um Programa que pergunte quanto você ganha por hora e o número de horas
# trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são
# descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um
# programa que nos dê: salário bruto. quanto pagou ao INSS. quanto pagou ao sindicato. o salário
# líquido. calcule os descontos e o salário líquido, conforme a tabela abaixo:
# + Salário Bruto : R$
# - IR (11%) : R$
# - INSS (8%) : R$
# - Sindicato (5%) : R$
# = Salário Liquido : R$
# Obs.: Salário Bruto - Descontos = Salário Líquido.

valor = float(input('Digite o seu ganho por hora: $'))
hora = float(input('Digite a quantidade de horas trabalhadas neste mês: '))
salarioBruto = valor * hora
ir = salarioBruto * 0.11
inss = salarioBruto * 0.08
sindicato = salarioBruto * 0.05
salarioLiquido = salarioBruto - ir - inss - sindicato
print(f'+ Salário Bruto: R${salarioBruto:.2f}\n', f'- IR (11%): R${ir:.2f} \n', f'- INSS (8%): R${inss:.2f}\n',
      f'- Sindicato (5%): R${sindicato:.2f}\n', f'= Salario Liquido: R${salarioLiquido:.2f}', sep='')
