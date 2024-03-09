# Questão 27. Faça um programa que mostra os números múltiplos de 3 e múltiplos de 7, no
# intervalo de 10 a 150.

# lista = [
#     numero
#     for numero in range(10, 151)
#     if numero % 3 == 0 or numero % 7 == 0
# ]
# print(lista)

def criaListaMultiplos(start, stop, numeroBase):
    listaMultiplos = [
        numero
        for numero in range(start, stop + 1)
        if numero % numeroBase == 0
    ]
    return listaMultiplos


start = 10
stop = 150
listaMultiploTres = criaListaMultiplos(start, stop, 3)
listaMultiploSete = criaListaMultiplos(start, stop, 7)
print('Multiplos 3: ', listaMultiploTres)
print('Multiplos 7: ', listaMultiploSete)
