# Questão 25. Faça um programa que mostra os números múltiplos de 3, no intervalo de 50 a 125
# e a soma desses valores.
lista = [
    numero
    for numero in range(50, 126)
    if numero % 3 == 0
]
print(lista)
print(sum(lista))
