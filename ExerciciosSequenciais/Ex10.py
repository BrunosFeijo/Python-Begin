# Questão 10. Faça um Programa que peça 2 números inteiros e um número real. Calcule e
# mostre:
#   o produto do dobro do primeiro com metade do segundo.
#   a soma do triplo do primeiro com o terceiro.
#   o terceiro elevado ao cubo.

int1 = int(input('Digite o primeiro número inteiro: '))
int2 = int(input('Digite o segundo número inteiro: '))
float1 = float(input('Digite um número real: '))

produto = (int1 * 2) * (int2/2)
soma = (int1 * 3) + float1
potencia = float1 ** 3

print(f'O produto do dobro do primeiro com metade do segundo é {produto:.2f}')
print(f'A soma do triplo do primeiro com o terceiro é {soma}')
print(f'O terceiro elevado ao cubo é {potencia:.2f}')