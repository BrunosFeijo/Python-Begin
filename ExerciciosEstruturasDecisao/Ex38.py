# Questão 38. Faça um programa que lê 8 valores, calcula:
# a soma dos valores,
# a média dos valores maiores que 20
# e mostra os resultados

def media(*args):
    soma = 0
    for valor in args:
        soma += valor

    return soma / len(args)

valores = []
while len(valores) < 8:
    digito = float(input('Digite um valor: '))
    valores.append(digito)

somaValores = sum(valores)
print(f'Soma Total: {somaValores}')

valoresMaioresQueVinte = [
    numero
    for numero in valores
    if numero > 20
]
if len(valoresMaioresQueVinte) > 0:
    print(f'Média dos números maiores que 20: {media(*valoresMaioresQueVinte):.2f}')
    print(f'Valores: {valoresMaioresQueVinte}')