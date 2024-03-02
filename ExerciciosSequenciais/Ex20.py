# Questão 20. Elabore um algoritmo que lê 4 valores inteiros e mostra:
#   a soma dos valores;
#   a subtração do 1o valor e o 2o valor;
#   a multiplicação dos 3 primeiros valores digitados;
#   a média dos valores;
#   o resultado da equação (1o valor + 2o valor) / (3o valor – 4o valor).

def somar(*args):
    soma = 0
    for valor in args:
        soma += valor
    return soma


def subtracao(n1, n2):
    return n1 - n2


def multiplicacao(*args):
    produto = 1
    for valor in args:
        produto *= valor
    return produto


def media(*args):
    tamanho = len(args)
    soma = 0
    for valor in args:
        soma += valor
    return soma / tamanho


def divisao(n1, n2):
    return n1 / n2


def main():
    int1 = int(input('Digite o 1° número: '))
    int2 = int(input('Digite o 2° número: '))
    int3 = int(input('Digite o 3° número: '))
    int4 = int(input('Digite o 4° número: '))

    print('-' * 30)
    print(f'Soma: {somar(int1, int2, int3, int4)}')
    print(f'Subtração (1°/2°): {subtracao(int1, int2)}')
    print(f'Multiplicacao (1°, 2°, 3°): {multiplicacao(int1, int2, int3)}')
    print(f'Média: {media(int1, int2, int3, int4)}')
    print(f'Equação ((1° + 2°)/(3° - 4°)): {divisao(somar(int1, int2), subtracao(int3, int4)):.2f}')


main()
