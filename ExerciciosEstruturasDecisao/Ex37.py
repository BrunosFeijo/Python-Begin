# Questão 37. Faça um programa que entra com 10 números inteiros e calcula a soma;
# Se a soma dos valores for par, mostra a soma e quantos valores pares foram digitados,
# senão mostra a soma e quantos valores ímpares foram digitados

valores = []
while len(valores) < 10:
    digito = float(input('Digite um valor: '))
    valores.append(digito)

somaValores = sum(valores)
print(f'Soma Total: {somaValores}')
if somaValores % 2 == 0:
    valoresPares = [
        numero
        for numero in valores
        if numero % 2 == 0
    ]
    print(f'Pares: {valoresPares}')
    print(f'Qtd: {len(valoresPares)}')
    print(f'Soma: {sum(valoresPares)}')
else:
    valoresImpares = [
        numero
        for numero in valores
        if numero % 2 != 0
    ]
    print(f'Ímpares: {valoresImpares}')
    print(f'Qtd: {len(valoresImpares)}')
    print(f'Soma: {sum(valoresImpares)}')
