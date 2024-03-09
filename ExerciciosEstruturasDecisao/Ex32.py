# Questão 32. Faça um programa que calcula a tabuada de um número
def tabuada(valor):
    i = 1
    while i <= 10:
        print(f'{valor} x {i} = {valor * i}')
        i += 1


valor = int(input('Digite um número: '))
tabuada(valor)
