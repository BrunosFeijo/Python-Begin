# Questão 21. Elabore um algoritmo que lê 3 valores, mostra os 3 valores, a soma e o produto.
def somar(*args):
    soma = 0
    for valor in args:
        soma += valor
    return soma

def multiplicacao(*args):
    produto = 1
    for valor in args:
        produto *= valor
    return produto

def main():
    int1 = int(input('Digite o 1° número: '))
    int2 = int(input('Digite o 2° número: '))
    int3 = int(input('Digite o 3° número: '))

    valores = [int1, int2, int3]
    print(f'Valores {valores}')
    print(f'Soma: {somar(*valores)}')
    print(f'Multiplicacao: {multiplicacao(*valores)}')

main()