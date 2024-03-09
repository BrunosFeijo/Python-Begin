# Questão 26. Faça um programa que mostra os números múltiplos de 5, no intervalo de 20 a 100.
lista = [
    numero
    for numero in range(20, 101)
    if numero % 5 == 0
]
print(lista)

