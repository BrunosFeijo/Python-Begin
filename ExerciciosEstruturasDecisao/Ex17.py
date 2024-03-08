# Questão 17. Faça um programa que mostra os valores a partir de um intervalo informado pelo
# usuário. Mostre quantos valores pares estão no intervalo e a soma deles, bem como quantos
# ímpares e a media desses valores; Atenção, teste se o usuário digitou valores válidos, por ex: 2 e 6
# irá mostrar 2, 3, 4, 5, 6; Entretanto, se o usuário digitar 6 e 2, não será possível mostrar valores
def verificaDigitos(num1, num2):
    if num1 < num2:
        return True
    return False


def dividirNumeros(listaCompleta):
    listaPar = []
    listaImpar = []
    for valor in listaCompleta:
        if valor % 2 == 0:
            listaPar.append(valor)
        else:
            listaImpar.append(valor)

    return listaPar, listaImpar


def printListaPar(listaCompleta):
    print('-' * 10 + 'Lista Par' + '-' * 10)
    print(f'Qtd: {len(listaCompleta)}')
    print(f'Soma: {sum(listaCompleta)}')
    print(f'Lista: {listaCompleta}')


def printListaImpar(listaCompleta):
    print('-' * 10 + 'Lista Ímpar' + '-' * 10)
    print(f'Qtd: {len(listaCompleta)}')
    print(f'Média: {media(*listaCompleta)}')
    print(f'Lista: {listaCompleta}')


def media(*args):
    tamanho = len(args)
    soma = 0
    for valor in args:
        soma += valor
    return soma / tamanho


start = int(input('Digite o início do intervalo: '))
stop = int(input('Digite o final do intervalo: '))
if verificaDigitos(start, stop):
    lista = range(start, stop + 1)
    listaPar, listaImpar = dividirNumeros(lista)
    printListaPar(listaPar)
    printListaImpar(listaImpar)

else:
    print(f'O intervalo não é válido: {start} > {stop}')
