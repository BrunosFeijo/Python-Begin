# Questão 39. Faça um programa que entra com 10 números inteiros, calcula a média dos
# números ímpares e mostra o resultado

valores = []
while len(valores) < 10:
    digito = float(input('Digite um valor: '))
    valores.append(digito)

valoresImpares = [
    valor
    for valor in valores
    if valor % 2 != 0
]

print(f'Média ímpares: {(sum(valoresImpares) / len(valoresImpares)):.2f}')
