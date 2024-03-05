# Questão 54. Escreva um algoritmo para ler o salário mensal e o percentual de reajuste. Calcular e
# escrever o valor do novo salário.
# [Exemplo de dados de entrada]
# 500 (salário mensal)
# 15 (percentual de reajuste)
# [Saída para os dados de entrada acima]
# 575 (salário reajustado)
def reajuste(salario, aumento):
    return salario + (salario * aumento) / 100


salario = float(input('Digite o salario: '))
aumento = float(input('Digite o percentual de reajuste: '))
salario = reajuste(salario, aumento)

print('Salario reajustado: R${:.2f}'.format(salario))