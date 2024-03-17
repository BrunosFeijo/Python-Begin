# Questão 7. Faça uma função que verifique se um valor é perfeito ou não. Um valor é dito perfeito
# quando ele é igual a soma dos seus divisores excetuando ele próprio. (Ex: 6 é perfeito, 6 = 1 + 2 + 3,
# que são seus divisores). A função deve retornar um valor booleano

def ehPerfeito(valor):
    divisores = calculaDividores(valor)
    print(f'Divisores: {divisores}')
    return sum(divisores) == valor


def calculaDividores(valor):
    lista = range(1, valor)
    divisor = []
    for i in lista:
        if valor % i == 0:
            divisor.append(i)

    return divisor


num = int(input('Digite um número: '))

if ehPerfeito(num):
    print(f'O valor {num} é perfeito')
else:
    print(f'O valor {num} não é perfeito')
