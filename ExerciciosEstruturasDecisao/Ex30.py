# Questão 30. Faça um programa que mostra os 35 primeiros números pares.
lista = []
i = 1
while len(lista) < 35:
    if i % 2 == 0:
        lista.append(i)
    i += 1

print(lista)