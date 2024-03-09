# Questão 3. Faça um programa que mostra na tela os números de 23 até 55 e mostra a soma
# dos valores.

lista = range(23,56)
soma = 0
for numero in lista:
    print(numero, end=' ')
    soma += numero

print(f'\nSoma: {soma}')