# Questão 25. Lê três números e mostra:
#   a soma dos dois primeiros números lidos,
#   a subtração dos dois últimos números lidos
#   a multiplicação dos 3 números

def multiplicar(*args):
    produto = 1
    for valor in args:
        produto *= valor
    return produto


def subtrair(n1, n2):
    return n1 - n2


numeros = [
    float(input('Digite o 1° número: ')),
    float(input('Digite o 2° número: ')),
    float(input('Digite o 3° número: '))
]
print(f'A soma dos dois primeiros números: {sum(numeros[:2])}')
print(f'A subtração dos dois últimos números: {subtrair(*numeros[-2:])}')
print(f'A multiplcação dos 3 números: {multiplicar(*numeros)}')