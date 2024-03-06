# Questão 8. Faça um programa que mostra na tela os números de 50 até 5 e mostra os valores
# ímpares.
lista = range(50, 4, -1)
listaImpar = lista[1::2]

print('-' * 10 + 'Todos os valores' + '-' * 10)
for valor in lista:
    print(valor, end=' ')

print()
print('-' * 10 + 'Valores Ímpares' + '-' * 10)
for valor in listaImpar:
    print(valor, end=' ')
