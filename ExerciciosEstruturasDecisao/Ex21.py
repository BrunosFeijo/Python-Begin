# Questão 21. Faça um programa que imprime os números de 1 a 20, mostra a soma dos valores
# pares

def criaListaPar(start, stop, *step):
    listaPar = [
        numero
        for numero in range(start, stop)
        if numero % 2 == 0
    ]
    return listaPar


def printListaPar(listaCompleta):
    print('-' * 10 + 'Lista Par' + '-' * 10)
    print(f'Qtd: {len(listaCompleta)}')
    print(f'Soma: {sum(listaCompleta)}')
    print(f'Lista: {listaCompleta}')


lista = criaListaPar(1, 21)
listaCompleta = list(range(1, 21))
print(listaCompleta)
printListaPar(lista)
