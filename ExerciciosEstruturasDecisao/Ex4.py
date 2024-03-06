# Questão 4. Faça um programa que mostra na tela a soma dos números pares de 1 até 50 e
# mostra quantos números foram utilizados para calcular a soma.
lista = range(2, 51, 2)
soma = 0
qtd = 0
for numero in lista:
    print(numero, end=' ')
    soma += numero
    qtd += 1

print(f'\nSoma: {soma}\nQuantidade: {qtd}')
