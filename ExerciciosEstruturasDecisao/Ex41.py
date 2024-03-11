# Questão 41. Faça um programa que calcula a soma dos números pares compreendidos entre 50
# e 150
numeros = [
    numero
    for numero in range(50,151)
    if numero % 2 == 0
]

print(numeros)
print(f'Soma: {sum(numeros)}')
