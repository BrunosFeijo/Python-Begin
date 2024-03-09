# Questão 28. Faça um programa que mostra os números múltiplos de 5 ou múltiplos de 6, no
# intervalo de 100 a 300.

def criaListaMultiplos(start, stop, numeroBase):
    listaMultiplos = [
        numero
        for numero in range(start, stop + 1)
        if numero % numeroBase == 0
    ]
    return listaMultiplos


start = 100
stop = 300
listaMultiplosCinco = criaListaMultiplos(start, stop, 5)
listaMultiplosSeis = criaListaMultiplos(start, stop, 6)
print('Multiplos 5:', listaMultiplosCinco)
print('Multiplos 6:', listaMultiplosSeis)
