# Questão 5. Faça um programa que mostra na tela os números de 1 até 10 e os números de 10
# até 1
lista = range(1, 11)
listaReverse = lista[::-1]
for valor in lista:
    print(valor, end=' ')
    print(listaReverse[valor - 1])
