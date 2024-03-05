# Questão 53. Joao recebeu seu salário de R$ 1200,00 e precisa pagar duas contas (C1=R$ 200,00 e
# C2=R$120,00) que estão atrasadas. Como as contas estão atrasadas, Joao terá de pagar multa de 2%
# sobre cada conta. Faca um algoritmo que calcule e mostre quanto restara do salário do Joao.
def calculaJuros(valor):
    juros = 0.02
    return valor + (valor * juros)


c1 = 200
c2 = 120
salario = 1200

c1 = calculaJuros(c1)
c2 = calculaJuros(c2)
salario = salario - c1 - c2

print(f'O que sobrou foi {salario:.2f}')