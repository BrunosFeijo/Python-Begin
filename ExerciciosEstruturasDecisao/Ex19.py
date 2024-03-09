# Questão 19. Faça um programa que mostra a soma dos valores pares e o produto dos valores
# ímpares, considerando que os valores estão entre 100 é um valor informado pelo usuário. Atenção,
# verifique se o valor digitado pelo usuário é válido!

start = 100


def verificarNumero(numero):
    global start
    if numero <= start:
        return False
    return True


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


def multiplicar(*args):
    produto = 1
    for valor in args:
        produto *= valor
    return produto


def printListaImpar(listaCompleta):
    print('-' * 10 + 'Lista Ímpar' + '-' * 10)
    print(f'Qtd: {len(listaCompleta)}')
    print(f'Produto: {multiplicar(*listaCompleta)}')
    print(f'Lista: {listaCompleta}')


stop = int(input('Digite um número inteiro maior que 100: '))
if verificarNumero(stop):
    lista = list(range(start, stop + 1))
    listaPar, listaImpar = dividirNumeros(lista)
    printListaPar(listaPar)
    printListaImpar(listaImpar)
else:
    print('Número inválido. Digite um número maior que 100: ')
