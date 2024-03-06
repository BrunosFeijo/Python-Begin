# Questão 11. Faça um programa que mostra os números entre 121 e 201 de 3 em 3 (usando
# WHILE).
lista = range(121, 202, 3)
i = 0
while i < len(lista):
    print(lista[i], end=' ')
    i += 1
