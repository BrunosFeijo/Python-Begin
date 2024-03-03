# Questão 45. O restaurante a quilo Bem-Bao cobra R$12,00 por cada quilo de refeição. Escreva
# um algoritmo que leia o peso do prato montado pelo cliente (em quilos) e imprima o valor a pagar.
# Assuma que a balança ja desconte o peso do prato
def calculaValor(peso):
    valorKg = 12
    return valorKg * peso


peso = float(input('Digite o peso da refeição: '))
print(f'O valor da refeição foi R${calculaValor(peso):.2f}')
