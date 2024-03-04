# Questão 51. Um funcionário recebe um salário fixo mais 4% de comissão sobre as vendas. Faca
# um algoritmo que receba o salário fixo de um funcionário e o valor de suas vendas, calcule e
# mostre a comissão e o salário final do funcionário.

def calculaSalarioTotal(fixo, vendas):
    comissao = vendas * 0.04
    return fixo + comissao, comissao


salario = float(input('Digite o valor do salário fixo: '))
vendas = float(input('Digite o valor das vendas: '))
salarioTotal, comissao = calculaSalarioTotal(salario, vendas)

print('-' * 40)
print('Fixo: R${:.2f}'.format(salario))
print('Vendas: R${:.2f}'.format(vendas))
print('Comissão: R${:.2f}'.format(comissao))
print('Salario Total: R${:.2f}'.format(salarioTotal))