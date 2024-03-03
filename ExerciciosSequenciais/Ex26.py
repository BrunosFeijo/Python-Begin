# Questão 26. Elabore um algoritmo que lê 3 valores, mostra:
#   a soma do 1o e do 3o valor,
#   a divisão do 3o pelo 2o valor,
#   o produto do 1o e 2o valor
#   a subtração do 2o e 3o valor.
def multiplicar(*args):
    produto = 1
    for valor in args:
        produto *= valor
    return produto


def subtrair(n1, n2):
    return n1 - n2


def divisao(n1, n2):
    return n1 / n2


numeros = [
    float(input('Digite o 1° número: ')),
    float(input('Digite o 2° número: ')),
    float(input('Digite o 3° número: '))
]
print('-' * 30)
print(f'A soma do 1o e do 3o valor: {sum(numeros[0:3:2])}')
print(f'A divisão do 3° pelo 2°: {divisao(*numeros[3:0:-1]):.2f}')
print(f'O produto do 1° e 2°: {multiplicar(*numeros[:2])}')
print(f'A subtração do 2° e 3°: {subtrair(*numeros[1:3])}')