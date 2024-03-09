# Questão 7. Faça um programa que mostra na tela a soma dos números ímpares de 20 até 50 e
# mostra o total de valores somados.
lista = range(21, 51, 2)
soma = 0
qtd = 0
for numero in lista:
    print(numero, end=' ')
    soma += numero
    qtd += 1

print(f'\nSoma: {soma}\nQuantidade: {qtd}')
